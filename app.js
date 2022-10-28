const request= require('request')
const geocode= require('../weather-app/utils/geocode')
const forecast=require('../weather-app/utils/forecast')
const address=process.argv[2]

//console.log(process.argv)
if(!address){
    console.log('Please provide an  address')
}else{
    geocode(address,(error,{latitude,longitude,location}={}) =>{
        if(error){
            return console.log(error)
        }
        forecast(latitude,longitude,(error,forecastdata) =>{
            if(error){
                return console.log(error)
            }
            console.log(location)
            console.log(forecastdata)
        })
    })
}