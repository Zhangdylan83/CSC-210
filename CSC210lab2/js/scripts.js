var sq1 = document.getElementById("sq1");
var sq2 = document.getElementById("sq2");
var sq3 = document.getElementById("sq3");
var sq4 = document.getElementById("sq4");

var sq5 = document.getElementById("sq5");
var sq6 = document.getElementById("sq6");
var sq7 = document.getElementById("sq7");
var sq8 = document.getElementById("sq8");

var sq9 = document.getElementById("sq9");
var sq10 = document.getElementById("sq10");
var sq11 = document.getElementById("sq11");
var sq12 = document.getElementById("sq12");

var sq13 = document.getElementById("sq13");
var sq14 = document.getElementById("sq14");
var sq15 = document.getElementById("sq15");
var sq16 = document.getElementById("sq16");

var tempSQ = null;
var match = false;
var count = 0
function flipMade(sq)
{
    var face = sq.querySelector('.face');
    var back = sq.querySelector('.back');

    if(count < 2 && back.style.display !== 'none'){
        count++
        if (back.style.display != 'none'){
            back.style.display = 'none';
            face.style.display = 'block';
            if (tempSQ === null) {
                tempSQ = sq; 
            }
            else if(count == 2){ 
                if(checkMatch(tempSQ, sq)){
                    setTimeout(function() {
                        tempSQ.remove()
                        sq.remove()
                        tempSQ = null;
                        count = 0;}, 1000)
                    }//end if
                else{
                    setTimeout(function() {
                    var tempBack = tempSQ.querySelector('.back');
                    var tempFace = tempSQ.querySelector('.face');
                    console.log(tempBack)
                    tempBack.style.display = 'block';
                    tempFace.style.display = 'none';

                    back.style.display = 'block';  
                    face.style.display = 'none';

                    tempSQ = null;
                    count = 0;}, 1000)
                }//end else

            }//end if 

        }//end outer else
    }//end function flip
}



function checkMatch(sq1, sq2)
{

    var img1 = sq1.querySelector('img.face');
    var img2 = sq2.querySelector('img.face');

     
     if (img1 && img2) {
        var src1 = img1.src;
        var src2 = img2.src;

        if(src1 === src2) {
            console.log("Match found!"); 
            return true;
        }
    }
    console.log("No match or error in elements.");
    return false;

}

sq1.addEventListener("click", function(){
    flipMade(sq1);
})
sq2.addEventListener("click", function(){
    flipMade(sq2);
})
sq3.addEventListener("click", function(){
    flipMade(sq3);
})
sq4.addEventListener("click", function(){
    flipMade(sq4);
})
sq5.addEventListener("click", function(){
    flipMade(sq5);
})
sq6.addEventListener("click", function(){
    flipMade(sq6);
})
sq7.addEventListener("click", function(){
    flipMade(sq7);
})
sq8.addEventListener("click", function(){
    flipMade(sq8);
})
sq9.addEventListener("click", function(){
    flipMade(sq9);
})
sq10.addEventListener("click", function(){
    flipMade(sq10);
})
sq11.addEventListener("click", function(){
    flipMade(sq11);
})
sq12.addEventListener("click", function(){
    flipMade(sq12);
})
sq13.addEventListener("click", function(){
    flipMade(sq13);
})
sq14.addEventListener("click", function(){
    flipMade(sq14);
})
sq15.addEventListener("click", function(){
    flipMade(sq15);
})
sq16.addEventListener("click", function(){
    flipMade(sq16);
})
