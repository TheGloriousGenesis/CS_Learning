const REPO = "CS_Learning";
const USER = "TheGloriousGenesis";
const API_BASE = `https://api.github.com/repos/${USER}/${REPO}/git/trees/main?recursive=1`;
const POSTS_PER_PAGE = 3;
let currentPage = 1;

async function fetchBlogPosts() {
  const blogContainer = document.getElementById("blogPosts");
  blogContainer.innerHTML = "<p>Loading...</p>";

  try {
    const res = await fetch(API_BASE);
    const data = await res.json();

    const postFiles = data.tree.filter(item =>
      /\/posts\/README.md$/.test(item.path)
    );

    const posts = await Promise.all(postFiles.map(async file => {
      const rawUrl = `https://raw.githubusercontent.com/${USER}/${REPO}/main/${file.path}`;
      const res = await fetch(rawUrl);
      const content = await res.text();
      const title = content.match(/^#\s(.+)/)?.[1] || file.path;
      const tags = content.match(/tags:\s*(.+)/i)?.[1]?.split(",")?.map(tag => tag.trim()) || [];

      return { title, tags, content };
    }));

    window.blogData = posts;
    displayPosts();
  } catch (err) {
    blogContainer.innerHTML = `<p>Error loading blog posts: ${err.message}</p>`;
  }
}

function displayPosts(filter = "") {
  const blogContainer = document.getElementById("blogPosts");
  blogContainer.innerHTML = "";
  const paginationContainer = document.getElementById("pagination");
  paginationContainer.innerHTML = "";

  const filtered = window.blogData.filter(post =>
    post.tags.some(tag => tag.toLowerCase().includes(filter.toLowerCase()))
  );

  const postsToDisplay = filter ? filtered : window.blogData;
  const totalPages = Math.ceil(postsToDisplay.length / POSTS_PER_PAGE);
  const start = (currentPage - 1) * POSTS_PER_PAGE;
  const end = start + POSTS_PER_PAGE;
  const pagePosts = postsToDisplay.slice(start, end);

  pagePosts.forEach(post => {
    const postEl = document.createElement("div");
    postEl.classList.add("card");

    postEl.innerHTML = `
      <h3>${post.title}</h3>
      <div>${post.tags.map(tag => `<span class="tag">${tag}</span>`).join(" ")}</div>
      <div>${marked.parse(post.content)}</div>
    `;

    blogContainer.appendChild(postEl);
  });

  if (totalPages > 1) {
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
