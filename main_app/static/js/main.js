const update_btn = document.querySelector("#comment-update");

update_btn.addEventListener("click", e => {
  console.log(`#${e.target.dataset.id}`);
  let commentEle = document.querySelector(`#${e.target.dataset.id}`);
  let commentValue = commentEle.innerText;
  let inputEle = document.createElement("input");
  inputEle.type = "text";
  inputEle.name = "text";

  let tag = ``;
  console.log(commentValue);
});
