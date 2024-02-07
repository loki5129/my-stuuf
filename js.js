const firebaseConfig = {
  apiKey: "AIzaSyCK3KmJsHt0rphWElFQqRs70owuMtiSAGE",
  authDomain: "test2-81b3d.firebaseapp.com",
  databaseURL: "https://test2-81b3d-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "test2-81b3d",
  storageBucket: "test2-81b3d.appspot.com",
  messagingSenderId: "595643878976",
  appId: "1:595643878976:web:46b1560bb58ac8598359a5",
  measurementId: "G-CKBJX9W75N"
};

function magic() {
  document.getElementById("magic").innerHTML = "magic.";
}


function dolly() {
  document.getElementById("dolly").innerHTML = "i hate";
  document.getElementById("dolly2").innerHTML = "JavaScript";
}



const PI = 3.14159265359;
let x = 5;
let y = 4;
let z = x*y;

// Numbers:
let length = 16;
let weight = 7.5;

// Strings:
let color = "Yellow";
let lastName = "Johnson";

// Booleans
let t = true;
let f = false;

// Object:
const joel={type:"ranger",rangercolor:"green",show:"lightspeed resuce"};
joel.year = 2000;
joel.rating = "6.4 stars";

// Array object:
const cars = ["Saab", "Volvo", "BMW"];

//exponetal

 let positive = 123e5;    // 12300000
 let negative = 123e-5;   // 0.00123


function base() {
  document.getElementById("base").innerHTML = PI;
}
function math() {
  document.getElementById("math").innerHTML = z;
}


function bol0() {
  document.getElementById("bol0").innerHTML = t;
}
function bol1() {
  document.getElementById("bol1").innerHTML = f;
}
function date() {
  document.getElementById("dat").innerHTML = date;
}
function sab() {
  document.getElementById("sab").innerHTML = cars;
}



function car() {
  document.getElementById("car").innerHTML = joel.rangercolor + " "+joel.type;
}


function car0() {
  document.getElementById("car0").innerHTML = joel.show;
}

function car1() {
  document.getElementById("car1").innerHTML = joel.year;
}

function car2() {
  document.getElementById("car2").innerHTML = joel.rating;
}

function ex() {
  document.getElementById("ex").innerHTML = positive;
}
function po() {
  document.getElementById("po").innerHTML = negative;
}
function ty() {
  document.getElementById("ty").innerHTML= typeof true;
}

function re(p1, p2) {
  return p1 * p2;
}
let result = re(2,2);
function tu() {
document.getElementById("tu").innerHTML = result;
}


let text = "abcdefghijklmnopqrstwvuxyz";
let part = text.slice(7, 13);
let parte = text.slice(22);
function tex() {
  document.getElementById("tex").innerHTML = text.length;
}

function let0() {
  document.getElementById("let0").innerHTML = text.charAt(0);
}
function sli() {
  document.getElementById('sli').innerHTML = part + " , " + parte;
}
