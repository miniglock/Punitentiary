const $updateBtns = $(".comment-update-btn");
const $cancelBtns = $(".comment-update-cancel-btn");

const HIDDEN_CLASS = "hidden";
const DATA_FORM = "form";
const DATA_ID = "id";

function commentUpdateBtnHandler() {
  let formId = $(this).data(DATA_FORM);
  let commentId = $(this).data(DATA_ID);
  let $form = $(`#${formId}`);
  let $comment = $(`#${commentId}`);
  $form.removeClass(HIDDEN_CLASS);
  $comment.addClass(HIDDEN_CLASS);
}

function commentUpdateCancelBtnHandler() {
  let formId = $(this).data(DATA_FORM);
  let commentId = $(this).data(DATA_ID);
  $(`#${formId}`).addClass(HIDDEN_CLASS);
  $(`#${commentId}`).removeClass(HIDDEN_CLASS);
}

$(document).ready(function() {
  $updateBtns.on("click", commentUpdateBtnHandler);
  $cancelBtns.on("click", commentUpdateCancelBtnHandler);
});
