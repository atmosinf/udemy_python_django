
var reset = document.querySelector("#b");

var cells = document.querySelectorAll("td");



function marker(){
  if(this.textContent === ''){
    this.textContent = 'X';
  }else if(this.textContent === 'X') {
    this.textContent = 'O';
  }else if(this.textContent === 'O'){
    this.textContent = '';
  }
  console.log('clicked!');
}

for (var i = 0; i < cells.length; i++) {
  cells[i].addEventListener('click', marker)
}



reset.addEventListener('click', function(){
  for (var i = 0; i < cells.length; i++) {
    cells[i].textContent = '';
  }
  console.log('reset!');
})

console.log('connected');
