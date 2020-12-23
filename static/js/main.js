// Configuration of 

Dropzone.autoDiscover =false;
const myDropzone= new Dropzone("#my-dz",{
    url:"upload/",
    maxFiles:2,
    maxFileSixes:2,
    acceptedFiles:'.jpg, .png',
})