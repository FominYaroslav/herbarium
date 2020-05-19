var canvas;
var ctx;
//{%load static %}


//var images = [ // собираем массив изображения
//
//    'images/pic1.jpg',
//    'images/pic2.jpg',
//    'images/pic3.jpg',
//    'images/pic4.jpg',
//    'images/pic5.jpg',
//    'images/pic6.jpg',
//    'images/pic7.jpg',
//    'images/pic8.jpg',
//    'images/pic9.jpg',
//    'images/pic10.jpg'
//];
var iActiveImage = 0;
$(function(){

    // рисуем активное изображение
    var image = new Image();
    image.onload = function () {
        ctx.drawImage(image, 0, 0, image.width*0.1, image.height*0.1); // создаём канву
    }
    image.crossOrigin = '';    
    image.src = crcr;
    console.log(image.src)

    // создаём объект
    canvas = document.getElementById('panel');
    ctx = canvas.getContext('2d');

    $('#panel').mousemove(function(e) { // перемещение мыши
        var canvasOffset = $(canvas).offset();
        var canvasX = Math.floor(e.pageX - canvasOffset.left);
        var canvasY = Math.floor(e.pageY - canvasOffset.top);

        var imageData = ctx.getImageData(canvasX, canvasY, 1, 1);
        var pixel = imageData.data;

        var pixelColor = "rgba("+pixel[0]+", "+pixel[1]+", "+pixel[2]+", "+pixel[3]+")";
        $('#preview').css('backgroundColor', pixelColor);
    });

    $('#panel').click(function(e) { // клик мыши
        var canvasOffset = $(canvas).offset();
        var canvasX = Math.floor(e.pageX - canvasOffset.left);
        var canvasY = Math.floor(e.pageY - canvasOffset.top);

        var imageData = ctx.getImageData(canvasX, canvasY, 1, 1);
        var pixel = imageData.data;

        $('#rVal').val(pixel[0]);
        $('#gVal').val(pixel[1]);
        $('#bVal').val(pixel[2]);

        $('#rgbVal').val(pixel[0]+','+pixel[1]+','+pixel[2]);
        $('#rgbaVal').val(pixel[0]+','+pixel[1]+','+pixel[2]+','+pixel[3]);
        var dColor = pixel[2] + 256 * pixel[1] + 65536 * pixel[0];
        $('#hexVal').val( '#' + dColor.toString(16) );
    }); 

//    $('#swImage').click(function(e) { // переключение изображений
//        iActiveImage++;
//        if (iActiveImage >= 10) iActiveImage = 0;
////        image.src = "https://www.wikihow.com/images_en/thumb/f/fc/Get-the-URL-for-Pictures-Step-1-Version-6.jpg/v4-728px-Get-the-URL-for-Pictures-Step-1-Version-6.jpg.webp";
////        image.src = 'https://media.mnn.com/assets/images/2015/08/union-wood-sunrise.jpg.653x0_q80_crop-smart.jpg'
//    });
});