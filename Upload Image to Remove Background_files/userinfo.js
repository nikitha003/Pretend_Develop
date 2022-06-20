function getUserInfo(){makeRequest({method:'GET',url:"/user/info/"}).then((response)=>{const user=JSON.parse(response);if(user.authenticated==true){$('#registerBtn').addClass('hidden');$('#loginBtn').addClass('hidden');$('#profileBtn').removeClass('hidden');$('#logoutBtn').removeClass('hidden');}
if(user.images.length){$("#uploadedImages").removeClass('hidden');user.images.forEach(img=>{$("#uploadedImagesRow").append('\
				<div class="col-xs-12 col-sm-4 col-md-3 thumbnail-container">\
				<a href="/editor/'+img.id+'/'+img.secret+'?v=01072021" class="thumbnail">\
				<img src="/editor/'+img.id+'/'+img.secret+'/thumb"></a>\
				</div>\
				');});}}).catch((err)=>{console.error('error!',err.statusText);});}