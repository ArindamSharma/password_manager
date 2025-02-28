document.getElementById('fetchUser').addEventListener('click', async () => {
	const userId = 1; // Example user ID
	const response = await fetch(`/api/user/${userId}`);
	const data = await response.text();
	document.getElementById('userData').innerText = data;
  });