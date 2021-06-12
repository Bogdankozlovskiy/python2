function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');




$("document").ready(
    function () {
        $(".comment-like").on("click", function () {
            let comment_id = $(this).attr("id");

            $.ajax({
                "url":"/shop/add-ajax-like/",
                "data":{
                    "comment_id": comment_id.split("_")[2],
                    "csrfmiddlewaretoken": csrftoken
                },
                "method": "post",
                success: function (data) {
                    $(`#${comment_id}`).html(`Likes: ${data}`)
                },
                error: function (data) {
                    console.log("hello error", data)
                }
            });
        })
    }
);