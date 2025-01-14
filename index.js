function GenerateKey(filename) {
  return fetch(filename)
    .then(response => response.text())
    .then(data => {
      const lines = data.split('\n');
      const randomIndex = Math.floor(Math.random() * lines.length);
      return lines[randomIndex].trim();
    });
}

function write_key_to_html(key, output_filename = 'key.html') {
  const html = `
<!DOCTYPE html>
<html>
<head>
  <title>Generated Key</title>
</head>
<body>
  <h1>Generated Key:</h1>
  <p>${key}</p>
</body>
</html>
`;
  const blob = new Blob([html], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = output_filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

async function main() {
  try {
    const key_file = 'list.txt'; // Replace with the actual path to your file
    const generated_key = await GenerateKey(key_file);
    await write_key_to_html(generated_key);
    console.log('Key generated and written to key.html');
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
