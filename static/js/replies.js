const editButtons = document.getElementsByClassName("btn-edit");
const replyText = document.getElementById("id_body");
const replyForm = document.getElementById("respondForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated replies ID upon click.
* - Fetches the content of the corresponding reply.
* - Populates the `replyText` input/textarea with the replies content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_reply/{replyId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let replyId = e.target.getAttribute("reply_id");
    let replyContent = document.getElementById(`reply${replyId}`).innerText;
    replyText.value = replyContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${replyId}`);
  });
}