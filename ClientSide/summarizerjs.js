const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');
const summarizeForm = document.getElementById('summarize-form');
const keywordInput = document.getElementById('keyword-input');
const summaryTextarea = document.getElementById('summary-textarea');
const paraInput = document.getElementById("parapaste-area")
const newBtn = document.getElementById("clickhere")
const uploadFile = document.getElementById("uploadfile")
let uploadedFile = null;

let fileAvailable = false



async function handleSummarize(){
  console.log(fileAvailable);
  if(fileAvailable){
    let ans = await getFileText(uploadedFile)
    let splittedArr = splitArr(ans)
    console.log(splittedArr);
    summaryTextarea.innerText = "loading..."
    console.log("hi");
    console.log(paraInput.value);
    console.log(keywordInput.value)
    axios.post("http://127.0.0.1:8000/summarizer",{
      
    "searchQuery": keywordInput.value,
    "paraArray": splittedArr
  
  }).then(response=>{
  summaryTextarea.innerText = response.data
  fileAvailable = false
  })

  }
  else{
    axios.post("http://127.0.0.1:8000/summarizer",{
      
    "searchQuery": keywordInput.value,
    "paraArray": splittedArr
  
  }).then(response=>{
  summaryTextarea.innerText = response.data
  fileAvailable = false
  })

  }
  



  
}

uploadFile.addEventListener("click",()=> {fileAvailable=true})

newBtn.addEventListener("click",handleSummarize)

async function getFileText(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      resolve(reader.result);
    };
    reader.onerror = reject;
    reader.readAsText(file);
  }).then(res =>{return res});
}



uploadForm.addEventListener('submit', (e) => {
  e.preventDefault();
  uploadedFile = fileInput.files[0];
});

function splitArr(para){
  let tempArr = para.split(/\r?\n/)
  return tempArr

}

