document.addEventListener("DOMContentLoaded", function(){

const form = document.getElementById("chat-form");
const typing = document.getElementById("typing");
const chatBox = document.getElementById("chat-box");

// auto scroll to bottom
if(chatBox){
chatBox.scrollTop = chatBox.scrollHeight;
}

// show typing when form submits
if(form){

form.addEventListener("submit", function(){

if(typing){
typing.style.display = "flex";
}

});

}

});