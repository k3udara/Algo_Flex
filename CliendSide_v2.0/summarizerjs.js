const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');
const summarizeForm = document.getElementById('summarize-form');
const keywordInput = document.getElementById('keyword-input');
const summaryTextarea = document.getElementById('summary-textarea');
const paraInput = document.getElementById("parapaste-area");
const newBtn = document.getElementById("summarize-btn"); //Just changed clickhere id to summarize-btn
const uploadFile = document.getElementById("uploadfile");
let uploadedFile = null;

let fileAvailable = false;

const errorText = "CNN.com will feature iReporter photos in a weekly Travel Snapshots gallery . Please submit your best shots of our featured destinations for next week . Visit CNN iReport.com/Travel next Wednesday for a new gallery of snapshots ."


async function handleSummarize(){
  console.log(fileAvailable);
  if(fileAvailable){
    let ans = await getFileText(uploadedFile)
    let splittedArr = splitArr(ans)
    console.log(splittedArr);
    summaryTextarea.innerText = "loading..."
    axios.post("http://127.0.0.1:8000/summarizer",{
      
    "searchQuery": keywordInput.value,
    "paraArray": splittedArr
  
  }).then(response=>{
    console.log(response.data);

    if(errorText !== response){
        summaryTextarea.innerText = response.data
        fileAvailable = false
        
    }
    else{
        summaryTextarea.innerText = "wrong query"
        fileAvailable = false
    }

  })

  }
  else{
    summaryTextarea.innerText = "loading..."
    axios.post("http://127.0.0.1:8000/summarizer",{
      
    "searchQuery": keywordInput.value,
    "paraArray": [paraInput.value]
  
  }).then(response=>{
    console.log(response.data);

    if(errorText != response){
        summaryTextarea.innerText = response.data
        fileAvailable = false
        
    }
    else{
        summaryTextarea.innerText = "wrong query"
        fileAvailable = false
    }

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

