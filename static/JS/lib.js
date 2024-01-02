function teacher()
{
    let a = document.getElementById("name").value;
    let b = document.getElementById("uname").value;
    let c = document.getElementById("pass").value;
    let d = document.getElementById("cpass").value;
    let e = document.getElementById("email").value;
    let f = document.getElementById("phone").value;
    


    var regexp = /^([A-Za-z0-9\.-]+)@([A-Za-z0-9\-]+).([a-z]{2,3})([a-z]{2,3})?$/;
    var phoneexp = /^\+?\d{1,4}?[-.\s]?([0-9]{10})$/;
    


    if(a=="")
    {
        document.getElementById("sname").innerHTML="Name cannot be null";
    }
    else
    {
        document.getElementById("sname").innerHTML= " ";
    }


    if(b=="")
    {
        document.getElementById("suname").innerHTML="Username cannot be null";
    }
    else
    {
        document.getElementById("suname").innerHTML= " ";
    }


    if(c=="")
    {
        document.getElementById("word").innerHTML="Password cannot be null";
    }
    else
    {
        document.getElementById("word").innerHTML= " ";
    }

    if(d=="")
    {
        document.getElementById("conword").innerHTML="Password cannot be null";
    }
    else
    {
        document.getElementById("conword").innerHTML= " ";
    }


    if(e=="")
    {
        document.getElementById("mail").innerHTML="Email cannot be null";
    }
    else if(!regexp.test(e))
    {
        document.getElementById("mail").innerHTML="Please Enter valid Email";   
    }
    else
    {
        document.getElementById("mail").innerHTML= " ";
    }


    if(f=="")
    {
        document.getElementById("mobile").innerHTML="Phone cannot be null";
    }
    else if(!phoneexp.test(f))
    {
        document.getElementById("mobile").innerHTML="Please enter valid Number";
    }
    else
    {
        document.getElementById("mobile").innerHTML= " ";
    }

    
}



function student()
{
    let g = document.getElementById("stud").value;
    let h = document.getElementById("studuser").value;
    let i = document.getElementById("studpass").value;
    let j = document.getElementById("confirm").value;
    let k = document.getElementById("maill").value;
    let l = document.getElementById("studmobile").value;


    var regexp = /^([A-Za-z0-9\.-]+)@([A-Za-z0-9\-]+).([a-z]{2,3})([a-z]{2,3})?$/;
    var phoneexp = /^\+?\d{1,4}?[-.\s]?([0-9]{10})$/;
    


    if(g=="")
    {
        document.getElementById("studid").innerHTML="Name cannot be null";
    }
    else
    {
        document.getElementById("studid").innerHTML= " ";
    }


    if(h=="")
    {
        document.getElementById("studname").innerHTML="ID cannot be null";
    }
    else
    {
        document.getElementById("studname").innerHTML= " ";
    }


    if(i=="")
    {
        document.getElementById("studword").innerHTML="Username cannot be null";
    }
    else
    {
        document.getElementById("studword").innerHTML= " ";
    }

    if(j=="")
    {
        document.getElementById("studconword").innerHTML="Password cannot be null";
    }
    else
    {
        document.getElementById("studconword").innerHTML= " ";
    }


    if(k=="")
    {
        document.getElementById("studmail").innerHTML="Email cannot be null";
    }
    else if(!regexp.test(k))
    {
        document.getElementById("studmail").innerHTML="Please Enter valid Email";
        
        
    }
    else
    {
        document.getElementById("studmail").innerHTML= " ";
    }


    if(l=="")
    {
        document.getElementById("studphone").innerHTML="Phone cannot be null";
    }
    else if(!phoneexp.test(l))
    {
        document.getElementById("studphone").innerHTML="Please enter valid Number";
    }
    else
    {
        document.getElementById("studphone").innerHTML= " ";
    }
}

function user()
{
    let u = document.getElementById("userr").value;
    let p = document.getElementById("passs").value;


    if(u=="")
    {
        document.getElementById("usee").innerHTML="Name cannot be null";
    }
    else
    {
        document.getElementById("usee").innerHTML= " ";
    }


    if(p=="")
    {
        document.getElementById("pause").innerHTML="ID cannot be null";
    }
    else
    {
        document.getElementById("pause").innerHTML= " ";
    }
}


function book()
{
    let a = document.getElementById("bkn").value;
    let b = document.getElementById("photo").value;
    let c = document.getElementById("bookn").value;
    let d = document.getElementById("bookc").value;
    let e = document.getElementById("bookauthor").value;
    let f = document.getElementById("pub").value;
    let g = document.getElementById("ret").value;
    let h = document.getElementById("fee").value;
   


    
    


    if(a=="")
    {
        document.getElementById("bkid").innerHTML="Name cannot be null";
    }
    else
    {
        document.getElementById("bkid").innerHTML= " ";
    }



    if(b=="")
    {
        document.getElementById("pic").innerHTML="Image cannot be null";
    }
    else
    {
        document.getElementById("pic").innerHTML= " ";
    }


    if(c=="")
    {
        document.getElementById("bkname").innerHTML="ID cannot be null";
    }
    else
    {
        document.getElementById("bkname").innerHTML= " ";
    }


    if(d=="")
    {
        document.getElementById("bkcat").innerHTML="Username cannot be null";
    }
    else
    {
        document.getElementById("bkcat").innerHTML= " ";
    }


    if(e=="")
    {
        document.getElementById("bkauthor").innerHTML="Username cannot be null";
    }
    else
    {
        document.getElementById("bkauthor").innerHTML= " ";
    }

    if(f=="")
    {
        document.getElementById("bpubl").innerHTML="Password cannot be null";
    }
    else
    {
        document.getElementById("bpubl").innerHTML= " ";
    }

    if(g=="")
    {
        document.getElementById("date").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("date").innerHTML= " ";
    }

    if(h=="")
    {
        document.getElementById("cash").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("cash").innerHTML= " ";
    }


    
}

function issueb()
{
    let a = document.getElementById("bid").value;
    let b = document.getElementById("nameb").value;
    let c = document.getElementById("userid").value;
    let d = document.getElementById("issued").value;
    let e = document.getElementById("retd").value;
   


   
    


    if(a=="")
    {
        document.getElementById("bkid").innerHTML="ID cannot be null";
    }
    else
    {
        document.getElementById("bkid").innerHTML= " ";
    }


    if(b=="")
    {
        document.getElementById("namebk").innerHTML="Name cannot be null";
    }
    else
    {
        document.getElementById("namebk").innerHTML= " ";
    }


    if(c=="")
    {
        document.getElementById("person").innerHTML="UserID cannot be null";
    }
    else
    {
        document.getElementById("person").innerHTML= " ";
    }

    if(d=="")
    {
        document.getElementById("issuedt").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("issuedt").innerHTML= " ";
    }


    if(e=="")
    {
        document.getElementById("retdt").innerHTML="field cannot be null";
    }
    
    else
    {
        document.getElementById("retdt").innerHTML= " ";
    }


   
    
}


function card()
{
    let a = document.getElementById("bkid").value;
    let b = document.getElementById("cid").value;


    if(a=="")
    {
        document.getElementById("bid").innerHTML="field cannot be null";
    }
    
    else
    {
        document.getElementById("bid").innerHTML= " ";
    }

    if(b=="")
    {
        document.getElementById("cdid").innerHTML="field cannot be null";
    }
    
    else
    {
        document.getElementById("cdid").innerHTML= " ";
    }
}
  





