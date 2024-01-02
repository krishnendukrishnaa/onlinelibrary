function RetStaff()
{
    let a = document.getElementById("input1").value;
    let b = document.getElementById("input2").value;
    let c = document.getElementById("input3").value;
    let d = document.getElementById("input4").value;
    let e = document.getElementById("input5").value;
    let f = document.getElementById("input6").value;
    let g = document.getElementById("input7").value;
    


    
    


    if(a=="")
    {
        document.getElementById("ret_user_id1").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("ret_user_id1").innerHTML= " ";
    }

    
    if(b=="")
    {
        document.getElementById("ret_id1").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("ret_id1").innerHTML= " ";
    }

    if(c=="")
    {
        document.getElementById("ret_name1").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("ret_name1").innerHTML= " ";
    }


    if(d=="")
    {
        document.getElementById("ret_id1_no").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("ret_id1_no").innerHTML= " ";
    }


    if(e=="")
    {
        document.getElementById("ret_issue_date1").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("ret_issue_date1").innerHTML= " ";
    }


    if(f=="")
    {
        document.getElementById("ret_Ret_date1").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("ret_Ret_date1").innerHTML= " ";
    }


    if(g=="")
    {
        document.getElementById("ret_ret_fine1").innerHTML="Field cannot be null";
    }
    else
    {
        document.getElementById("ret_ret_fine1").innerHTML= " ";
    } 

    
}