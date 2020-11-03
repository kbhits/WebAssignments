function goBack()
{
	window.history.back()
}

var myVar = setInterval(function(){myTimer()}, 1000);
function myTimer()
{
    var d = new Date();
    var t = d.toLocaleTimeString();
    document.getElementById("demo").innerHTML = t;
}

class Snowflake{
    constructor(){
        this.init();//构造函数，调用定义好的init()方法;
    }
    init(){
        this.position={   //雪花对象的位置;
            x:Math.random()*width,//x坐标随机;
            y:Math.random()*height,//y坐标随机;
        }
        this.speed=Math.random()*10;//雪花下落速度为0-10以内的随机数;
        this.r=Math.random()*6;//雪花的半径为0-6以内的随机数;
        this.transparency=Math.random();//设置雪花的透明度为随机;
        this.color={
            r1:Math.random()*255,//雪花颜色随机;
            g:Math.random()*255,
            b:Math.random()*255,
        }
    }
    draw(){//雪花绘制方法;
        this.position.y++;//y坐标每次递增1像素;
        this.transparency-=0.01;//透明度每次递减0.01;
        if(this.transparency<=0){//透明度小于0，即雪花消失，重新绘制雪花;
            this.init();
        }
        context.beginPath();//开始一个新的图形绘制;
        context.fillStyle="rgba("+this.color.r1+","+this.color.g+","+this.color.b+","+this.transparency+")";//根据类模型绘制圆形雪花;
        context.arc(this.position.x,this.position.y,this.r,0,Math.PI*2);//填充雪花的颜色;
        context.fill();
    }	
}

function cartoon(){
    context.clearRect(0,0,width,height);//动画完成一次进行清屏操作;
    for(var j=0;j<snowArray.length;j++){
        snowArray[j].draw();//将实例化好的每个雪花对象在画布上画出来;
    }
    requestAnimationFrame(cartoon);//递归调用动画效果;
}