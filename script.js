const REPO = "CS_Learning";
const USER = "TheGloriousGenesis";
const API_BASE = `https://api.github.com/repos/${USER}/${REPO}/git/trees/gh-pages?recursive=1`;
const POSTS_PER_PAGE = 3;
let currentPage = 1;
let allPosts = [];

function getQueryParam(name) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(name);
}

async function fetchBlogPosts() {
  const postContainer = document.getElementById("blogPosts");
  const fullPostContainer = document.getElementById("fullPost");
  const paginationContainer = document.getElementById("pagination");

  postContainer.innerHTML = "<p>Loading...</p>";
  if (fullPostContainer) fullPostContainer.innerHTML = "";
  if (paginationContainer) paginationContainer.innerHTML = "";

  try {
    const res = await fetch(API_BASE);
    const data = await res.json();

    const postFiles = data.tree.filter(item =>
      /\/posts\/README\.md$/i.test(item.path)
    );

    const posts = await Promise.all(postFiles.map(async file => {
      const rawUrl = `https://raw.githubusercontent.com/${USER}/${REPO}/gh-pages/${file.path}`;
      const res = await fetch(rawUrl);
      const content = await res.text();
      const title = content.match(/^#\s(.+)/)?.[1] || file.path;
      const tags = content.match(/tags:\s*(.+)/i)?.[1]?.split(",")?.map(tag => tag.trim()) || [];
      const summary = content.split('\n').find(line => line && !line.startsWith("#") && !line.startsWith("tags")) || "";
      return { title, tags, content, summary, path: file.path };
    }));

    allPosts = posts;
    const postPath = getQueryParam("path");
    if (postPath) {
      showFullPost(postPath);
    } else {
      displayPosts();
    }

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

  blogContainer.style.display = "grid";
  paginationContainer.style.display = "flex";
  if (sidebar) sidebar.style.display = "block";
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

  if (totalPages > 1) {
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
}

function showFullPost(path) {
  const post = allPosts.find(p => p.path === path);
  if (!post) return;

  document.body.classList.add("post-mode");

  const blogContainer = document.getElementById("blogPosts");
  const paginationContainer = document.getElementById("pagination");
  const fullPostContainer = document.getElementById("fullPost");
  const sidebar = document.querySelector(".sidebar");

  blogContainer.style.display = "none";
  paginationContainer.style.display = "none";
  if (sidebar) sidebar.style.display = "none";

  const md = window.markdownit().use(window.markdownitAdmonition);
  const html = md.render(post.content);

  window.scrollTo(0, 0);

  fullPostContainer.innerHTML = `
    <a class="back-to-blog" href="blog.html">← Back</a>
    <article class="markdown-body post-content">
      ${html}
    </article>
  `;
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
