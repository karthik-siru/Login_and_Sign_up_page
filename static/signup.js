// this javascript file is to check whether the email is valid or not 
// and to pick a strong password 


function validate(){


   var user      =  document.getElementById('name');
   var email     =  document.getElementById('email');
   var password  =  document.getElementById('pswd');
   var passwordc =  document.getElementById('pswdc');
   let u= 0,e= 0,p=0 ,pc =0  ;

    if (user.value.trim() == ""){
        user.style.border = "1px solid red" ;
        u = 1
    }
    if (email.value.trim() == ""){
        email.style.border = "1px solid red" ;
        e = 1
    }
    if (password.value.trim() == ""){
        password.style.border = "1px solid red" ;
        p =1
    }
    if (password.value.trim() == ""){
        passwordc.style.border = "1px solid red" ;
        pc = 1
    }

    if (u || e || p || pc )
        return false ;    

    if (password.value.trim() == passwordc.value.trim() )
        return true ;
    else 
    {   
        passwordc.style.border = "1px solid red" ;
        passwordc.innerHTML = "not same as above";
        return false ;
    }
}


