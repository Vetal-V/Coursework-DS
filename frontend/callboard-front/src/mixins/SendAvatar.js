$('#profile-photo').on('submit', function(e) {
    e.preventDefault();

var form = $('#profile-photo')[0];
var formData = new FormData(form);

 jQuery.each(jQuery('#photo-filename')[0].files, function(i, file) {
    formData.append('file-'+i, file);
});

$.ajax({
  url: "http://127.0.0.1:8000/profile/update/avatar/1/",
  data: formData,
  type: "PUT",
  contentType: false,
  cache: false,
  processData: false
});

    console.log(formData);
});
