const mouseWheelEvt = function (event) {
            if (document.getElementById("frame").style.flexDirection=="row-reverse"){
                if (document.body.doScroll)
                    document.body.doScroll(event.wheelDelta>0?"left":"right");
                else if ((event.wheelDelta || event.detail) > 0)
                    window.scrollBy({ left: 500, behavior: 'smooth' });
                else
                    window.scrollBy({ left: -500, behavior: 'smooth' });
                    // alert("works");
                    return false;
                }
            }
            window.addEventListener("wheel", event => mouseWheelEvt(event));

            // var fliped = false;
            document.addEventListener("keydown", function(event) {
                // alert(event.keyCode);
                switch(event.keyCode) {
                    case 84:  // T key
                        if (document.getElementById("frame").style.flexDirection=="column") {
                            document.getElementById("frame").style.flexDirection="row-reverse";
                            document.getElementById("frame").style.overflow="hidden";
                            document.getElementById("frame").style.paddingLeft=document.body.scrollWidth;
                        

                        } else {
                            document.getElementById("frame").style.flexDirection="column";
                            }
                        window.scrollTo({ top: 0, left: document.body.scrollWidth, behavior: 'smooth' });
                        

                        break;
                    case 37:  // <- key
                        // document.body.scrollLeft -= 800;
                        window.scrollBy({ top: 0, left: -800, behavior: 'smooth' });
                        break;
                    case 39:  // -> key
                        // document.body.scrollLeft += 800;
                        window.scrollBy({ top: 0, left: 800, behavior: 'smooth' });
                        break;
                    case 96:  // 0 key
                        window.scrollTo({ top: 0, left: document.body.scrollWidth, behavior: 'smooth' });
                        break;
                    case 97:  // 1 key
                        window.scrollTo({ top: document.body.scrollHeight, left: 0, behavior: 'smooth' });
                        break;
                    case 72:  // H key
                        alert("T -toggle, <- -left, -> -right, 0 -start, 1 -end, H -help");
                        break;
                    case 83:  // S key
                        window.location.href = "/side";
                        break;
                    
                        
                    
                
                }
            });