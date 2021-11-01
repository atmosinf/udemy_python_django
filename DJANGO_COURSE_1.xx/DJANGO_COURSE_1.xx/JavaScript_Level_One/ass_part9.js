var fname = prompt("Please enter your first name");
var lname = prompt("Please enter your last name");
var age = prompt("Please enter your age");
var height = prompt("Please enter your height");
var petname = prompt("Please enter your petname");

if (fname[0] === lname[0] && age > 20 && age < 30 && height > 170 && petname[petname.length-1] === 'y'){
  console.log("Welcome comrade to the spy agency!");
}else{
  console.log("Nothing to see here");
}
