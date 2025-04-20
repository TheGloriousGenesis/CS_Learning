const REPO = "tech_learning";
const USER = "TheGloriousGenesis";
const API_BASE = `https://api.github.com/repos/${USER}/${REPO}/git/trees/main?recursive=1`;
const POSTS_PER_PAGE = 3;
let currentPage = 1;
let allPosts = [];

const md = window.markdownit({
  highlight: function (str, lang) {
    if (window.hljs && lang && hljs.getLanguage(lang)) {
      try {
        return `<pre><code class="hljs language-${lang}">${hljs.highlight(str, { language: lang }).value}</code></pre>`;
      } catch (__) {}
    }
    return `<pre><code class="hljs">${md.utils.escapeHtml(str)}</code></pre>`;
  }
});

md.use(window.markdownitAdmon); // optional, for [!NOTE] etc.

function getQueryParam(name) {
  return new URLSearchParams(window.location.search).get(name);
}

async function fetchBlogPosts() {
  const postContainer = document.getElementById("blogPosts");
  const fullPostContainer = document.getElementById("fullPost");
  const paginationContainer = document.getElementById("pagination");
  const searchBox = document.querySelector(".search-box");

  // Move search box above card grid
  if (searchBox && postContainer) {
    postContainer.parentNode.insertBefore(searchBox, postContainer);
    searchBox.style.display = "block";
  }

  postContainer.innerHTML = "<p>Loading...</p>";
  fullPostContainer.innerHTML = "";
  paginationContainer.innerHTML = "";

  try {
    const res = await fetch(API_BASE);
    const data = await res.json();

    const postFiles = data.tree.filter(item => /\/posts\/README\.md$/i.test(item.path));

    const posts = await Promise.all(postFiles.map(async file => {
      const rawUrl = `https://raw.githubusercontent.com/${USER}/${REPO}/main/${file.path}`;
      const res = await fetch(rawUrl);
      const content = await res.text();
      const title = content.match(/^#\s(.+)/)?.[1] || file.path;
      const tags = content.match(/tags:\s*(.+)/i)?.[1]?.split(",")?.map(tag => tag.trim()) || [];
      const summary = content.split('\n').find(line => line && !line.startsWith("#") && !line.startsWith("tags")) || "";
      return { title, tags, content, summary, path: file.path };
    }));

    allPosts = posts;
    const postPath = getQueryParam("path");
    postPath ? showFullPost(postPath) : displayPosts();

  } catch (err) {
    postContainer.innerHTML = `<p>Error loading blog posts: ${err.message}</p>`;
  }
}

function displayPosts(filter = "") {
  document.body.classList.remove("post-mode");

  const blogContainer = document.getElementById("blogPosts");
  const paginationContainer = document.getElementById("pagination");
  const fullPostContainer = document.getElementById("fullPost");
  const sidebar = document.querySelector(".sidebar");
  const searchBox = document.querySelector(".search-box");

  blogContainer.style.display = "grid";
  paginationContainer.style.display = "flex";
  if (sidebar) sidebar.style.display = "block";
  if (searchBox) searchBox.style.display = "block";
  fullPostContainer.innerHTML = "";

  const filtered = allPosts.filter(post =>
    post.tags.some(tag => tag.toLowerCase().includes(filter.toLowerCase()))
  );

  const postsToDisplay = filter ? filtered : allPosts;
  const totalPages = Math.ceil(postsToDisplay.length / POSTS_PER_PAGE);
  const start = (currentPage - 1) * POSTS_PER_PAGE;
  const end = start + POSTS_PER_PAGE;
  const pagePosts = postsToDisplay.slice(start, end);

  blogContainer.innerHTML = "";

  pagePosts.forEach(post => {
    const postEl = document.createElement("div");
    postEl.classList.add("card");

    postEl.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.summary}</p>
      <div>${post.tags.map(tag => `<span class="tag">${tag}</span>`).join(" ")}</div>
      <a href="blog.html?path=${encodeURIComponent(post.path)}">Read more</a>
    `;

    blogContainer.appendChild(postEl);
  });

  paginationContainer.innerHTML = "";
  for (let i = 1; i <= totalPages; i++) {
    const btn = document.createElement("button");
    btn.textContent = i;
    if (i === currentPage) btn.disabled = true;
    btn.onclick = () => {
      currentPage = i;
      displayPosts(filter);
    };
    paginationContainer.appendChild(btn);
  }
}

function showFullPost(path) {
  const post = allPosts.find(p => p.path === path);
  if (!post) return;

  document.body.classList.add("post-mode");

  const blogContainer = document.getElementById("blogPosts");
  const paginationContainer = document.getElementById("pagination");
  const fullPostContainer = document.getElementById("fullPost");
  const sidebar = document.querySelector(".sidebar");
  const searchBox = document.querySelector(".search-box");

  blogContainer.style.display = "none";
  paginationContainer.style.display = "none";
  if (sidebar) sidebar.style.display = "none";
  if (searchBox) searchBox.style.display = "none";

  const html = md.render(post.content);
  const doc = new DOMParser().parseFromString(html, 'text/html');
  const headings = doc.querySelectorAll('h2, h3');

  const toc = Array.from(headings).map(h => {
    const id = h.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-');
    h.id = id;
    return `<li class="toc-${h.tagName.toLowerCase()}" data-target="${id}"><a href="#${id}">${h.textContent}</a></li>`;
  }).join('');

  window.scrollTo(0, 0);

  fullPostContainer.innerHTML = `
    <a class="back-to-blog" href="blog.html">← Back</a>
    <div class="post-layout">
      <aside class="post-toc">
        <h3>SUMMARY</h3>
        <ul>${toc}</ul>
      </aside>
      <article class="markdown-body post-content">${doc.body.innerHTML}</article>
    </div>
  `;

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const id = entry.target.getAttribute('id');
      const tocLink = document.querySelector(`.post-toc li[data-target="${id}"]`);
      if (entry.isIntersecting) {
        document.querySelectorAll(".post-toc li").forEach(li => li.classList.remove("active"));
        if (tocLink) tocLink.classList.add("active");
      }
    });
  }, { rootMargin: "-50% 0px -50% 0px", threshold: 0 });

  document.querySelectorAll(".post-content h2, .post-content h3").forEach(section => {
    observer.observe(section);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("searchInput");
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      currentPage = 1;
      displayPosts(this.value);
    });
  }

  if (document.getElementById("blogPosts")) fetchBlogPosts();
});
