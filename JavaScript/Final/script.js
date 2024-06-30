document.addEventListener("DOMContentLoaded", () => {
	const postContainer = document.getElementById("post-container");

	fetch("https://dummyjson.com/posts")
		.then((response) => response.json())
		.then((data) => {
			data.posts.slice(0, 10).forEach((post) => {
				const postElement = document.createElement("div");
				postElement.classList.add("post");
				postElement.innerHTML = `
                    <h2>${post.title}</h2>
                    <p>${post.body}</p>
                `;
				postContainer.appendChild(postElement);
			});
		})
		.catch((error) => console.error("Error fetching posts:", error));
});
