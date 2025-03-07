const editButtons = document.getElementsByClassName("btn-edit");
const replyText = document.getElementById("id_body");
const replyForm = document.getElementById("respondForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated reply's ID upon click.
* - Fetches the content of the corresponding reply.
* - Populates the `replyText` input/textarea with the reply's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_reply/{replyId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let replyId = e.target.getAttribute("reply_id");
    // console.log("this is reply ID", replyId);
    let replyContent = document.getElementById(`reply${replyId}`).innerText;
    // console.log("this is reply content", replyContent);
    replyText.value = replyContent;
    submitButton.innerText = "Update";
    respondForm.setAttribute("action", `edit_reply/${replyId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated reply's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let replyId = e.target.getAttribute("reply_id");
    deleteConfirm.href = `delete_reply/${replyId}`;
    deleteModal.show();
  });
}