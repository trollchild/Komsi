

//scrolli efekti


          //scrolli efekti
          var prevScrollpos = window.pageYOffset;
          window.onscroll = function() {
            var currentScrollPos = window.pageYOffset;

            if (prevScrollpos > currentScrollPos) {
                if(window.scrollY<50){
                  document.getElementById("topNav").style.backgroundColor = "rgba(0, 8, 1, 1.0)";
                  document.getElementById("topNav").style.transition = "background-Color 2.0s";
                }else{
                  document.getElementById("topNav").style.backgroundColor = "rgba(0, 8, 1, 0.9)";
                }
              document.getElementById("topNav").style.top = "0";

            }
              else{
              document.getElementById("topNav").style.top = "-65px";
            }
            prevScrollpos = currentScrollPos;
          }

          // nää pitäis olla vaan mobilessa esillä eli avaa sen menun
          function openNav() {
              document.getElementById("myNav").style.width = "100%";
          }

          function closeNav() {
              document.getElementById("myNav").style.width = "0%";
          }
