const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');
const summarizeForm = document.getElementById('summarize-form');
const keywordInput = document.getElementById('keyword-input');
const summaryTextarea = document.getElementById('summary-textarea');

let uploadedFile = null;

uploadForm.addEventListener('submit', (e) => {
  e.preventDefault();
  uploadedFile = fileInput.files[0];
});

summarizeForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const keyword = keywordInput.value;
  if (uploadedFile) {
    const text = await getFileText(uploadedFile);
    const summary = summarizeText(text, keyword);
    summaryTextarea.value = summary;
  }
});

function getFileText(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      resolve(reader.result);
    };
    reader.onerror = reject;
    reader.readAsText(file);
  });
}

function summarizeText(text, keyword) {
  // Should replace this placeholder function with our summarization logic
  return `Here is a summary of the text related to "${keyword}":\n\n${text.slice(0, 100)}...`;
}
