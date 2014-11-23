
    function initialize(dat) {
        console.log(dat);
        
        console.log(dat[0]);
        var arrLen = dat.length;
        for (var i = 0; i< arrLen; i++){
            
            var foodtruck = dat[i];
            console.log(foodtruck['applicant']);
            
            
        }
    }
        initialize({{ dat | tojson | safe}});
        
      // Create the map.
        </script>