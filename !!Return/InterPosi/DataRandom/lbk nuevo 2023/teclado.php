<head>
 



	
</head>

<script>
function agrega(x){
document.getElementById('cve').value=document.getElementById('cve').value +x;
	
	
}
function borra(){
str=document.getElementById('cve').value;
str = str.substring(0, str.length - 1);
document.getElementById('cve').value=str;
	
}

</script>
<style>

#webkeyboad {
    position: relative;
}

#webkeyboad .itec {
    cursor: pointer;
    background-color: #fff;
    border: 1px solid #e4e5e6;
    border-radius: 4px;
    color: #424242;
    -webkit-transition: all .1s ease-out;
    transition: all .1s ease-out;
    text-align: center;
    vertical-align: middle;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    width: 20px;
    height: 25px;
    font-weight: 600;
    margin-right: 2px;
    padding: 5px 0px;
    font-size: 15px;
}

#webkeyboad .idel {
    cursor: pointer;
    background-color: #fff;
    border: 1px solid #e4e5e6;
    border-radius: 4px;
    color: #424242;
    -webkit-transition: all .1s ease-out;
    transition: all .1s ease-out;
    text-align: center;
    vertical-align: middle;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    width: 26px;
    font-weight: 600;
    margin-right: 2px;
    padding: 5px 0px;
    font-size: 15px;
    background-image: url('./wp-content/i_delete.svg');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    background-position: center center;
}
#webkeyboad .itec:hover {
	background-color:#00bb31!important;
	
}
#webkeyboad .itec:last-child {
    margin-right: 0px;
}

#webkeyboad .mback {
    margin-bottom: 2px;
}

@media (max-width: 780px) {
    #webkeyboad {
        position: fixed;
        bottom: 0px;
        z-index: 500;
        width: 100%;
        left: 0px;
        min-height: 120px;
        box-shadow: 0 1px 9px rgb(0 0 0 / 37%);
        height: 150px;
        background: #fff;
        text-align: center;
        padding: 14px 0;
    }
    #webkeyboad .itec {
        width: 8.8%;
        min-height: 24px;
    }
    #webkeyboad .idel {
        height: 24px;
        width: 8.8%;
    }
}
.justify-content-center {
    justify-content: center!important;
}
.d-flex {
    display: flex!important;
}
.boadhide {
    position: absolute;
    top: -30px;
    left: 50%;
    -webkit-transform: translateX(-50%);
    transform: translateX(-50%);
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    border-bottom-style: none;
    min-height: 0;
    height: 29px;
    display: none;
    background-color: #fff;
    border: 1px solid #e4e5e6;
    border-radius: 4px;
    color: #8e8f90;
    -webkit-transition: all .1s ease-out;
    transition: all .1s ease-out;
    width: 8.8%;
}

.boadhide i::before {
    content: "\E004";
    font-family: icon-svg;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-style: normal;
    font-variant: normal;
    font-weight: 400;
    text-decoration: none;
    text-transform: none;
}

@media (max-width: 780px) {
    .boadhide {
        display: block !important;
    }
</style>                                    
                               
<div id="webkeyboad" class="noshsow" style="display:none;" onfocusout="jQuery('#webkeyboad').hide();" >
    <center><div onclick="jQuery('#webkeyboad').hide();" ><img src="./wp-content/cerrar.png" style="width: 20px;"></div></center>
    <div class="d-flex justify-content-center mback">
        <div onclick="agrega('0');" class="itec">0</div>
        <div onclick="agrega('1');" class="itec">1</div>
        <div onclick="agrega('2');" class="itec">2</div>
        <div onclick="agrega('3');" class="itec">3</div>
        <div onclick="agrega('4');" class="itec">4</div>
        <div onclick="agrega('5');" class="itec">5</div>
        <div onclick="agrega('6');" class="itec">6</div>
        <div onclick="agrega('7');" class="itec">7</div>
        <div onclick="agrega('8');" class="itec">8</div>
        <div onclick="agrega('9');" class="itec">9</div>
    </div>
    <div class="d-flex justify-content-center mback">
        <div onclick="agrega('Q');" class="itec">Q</div>
        <div onclick="agrega('W');" class="itec">W</div>
        <div onclick="agrega('E');" class="itec">E</div>
        <div onclick="agrega('R');" class="itec">R</div>
        <div onclick="agrega('T');" class="itec">T</div>
        <div onclick="agrega('Y');" class="itec">Y</div>
        <div onclick="agrega('U');" class="itec">U</div>
        <div onclick="agrega('I');" class="itec">I</div>
        <div onclick="agrega('O');" class="itec">O</div>
        <div onclick="agrega('P');" class="itec">P</div>
    </div>
    <div class="d-flex justify-content-center mback">
        <div onclick="agrega('A');" class="itec">A</div>
        <div onclick="agrega('S');" class="itec">S</div>
        <div onclick="agrega('D');" class="itec">D</div>
        <div onclick="agrega('F');" class="itec">F</div>
        <div onclick="agrega('G');" class="itec">G</div>
        <div onclick="agrega('H');" class="itec">H</div>
        <div onclick="agrega('J');" class="itec">J</div>
        <div onclick="agrega('K');" class="itec">K</div>
        <div onclick="agrega('L');" class="itec">L</div>
    </div>
    <div class="d-flex justify-content-center">
        <div onclick="agrega('Z');" class="itec">Z</div>
        <div onclick="agrega('X');" class="itec">X</div>
        <div onclick="agrega('C');" class="itec">C</div>
        <div onclick="agrega('V');" class="itec">V</div>
        <div onclick="agrega('B');" class="itec">B</div>
        <div onclick="agrega('N');" class="itec">N</div>
        <div onclick="agrega('M');" class="itec">M</div>
        <div onclick="borra();" class="idel" id="idel"></div>
    </div>
   
</div>