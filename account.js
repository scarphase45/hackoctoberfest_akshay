const sgMail = require('@sendgrid/mail') 

sgMail.setApiKey(process.env.SENDGRID_API_KEY)

const sendwelcomeEmail = (email,username) =>{
    // console.log(email) 
    sgMail.send({
        to:email,
        from:'amalreji017@gmail.com',
        subject:'Thanks for Signing up',
        text: `Thank you for Signing up,${username}`
    })
}

const sendRequestBlood = (email,username,bloodGroup,Hospital,) =>{
    sgMail.send({
        to:email,
        from:'amalreji017@gmail.com',
        subject:`Request for ${bloodGroup} Group`,
        text:`Hi ${username},There is a requirement for ${bloodGroup} group at ${Hospital}.Kindly login and accept the request if available`
    })
}

const sendDeleteEmail = (email,username) =>{
    // console.log(email) 
    sgMail.send({
        to:email,
        from:'amalreji017@gmail.com',
        subject:'Account Deletion',
        text: `Sorry to see you leave,${username}`
    })
}

module.exports = {
    sendwelcomeEmail,
    sendDeleteEmail,
    sendRequestBlood
}