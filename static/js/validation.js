var count = 0;
$("#btn_sbt").click(function () {
    var gre_score = $("#gre_score").val();
    var toefl_score = $("#toefl_score").val();
    var university_rating = $("#university_rating").val();
    var sop = $("#sop").val();
    var lor = $("#lor").val();
    var cgpa = $("#cgpa").val();
    checkNullField(gre_score, 1);
    checkNullField(toefl_score, 2);
    checkNullField(university_rating, 3);
    checkNullField(sop, 4);
    checkNullField(lor, 5);
    checkNullField(cgpa, 6);

    if (count > 0) {
        alert("Fill all details");
        return false;

    } else {
        return true;
    }
});
function checkNullField(id, val) {

    if (id == "" || id == null) {
        count++;
        addCssError(val);
    } else {
        addCssSucess(val);
    }
}
function addCssError(val) {
    return (val == 1) ? $("#gre_score").addClass("errorMessage")
        : (val == 2) ? $("#toefl_score").addClass("errorMessage")
            : (val == 3) ? $("#university_rating").addClass("errorMessage")
                : (val == 4) ? $("#sop").addClass("errorMessage")
                    : (val == 5) ? $("#lor").addClass("errorMessage")
                        : (val == 6) ? $("#cgpa").addClass("errorMessage")
                            : "";
}
function addCssSucess(val) {
    return (val == 1) ? $("#gre_score").addClass("successMessage")
        : (val == 2) ? $("#toefl_score").addClass("successMessage")
            : (val == 3) ? $("#university_rating").addClass("successMessage")
                : (val == 4) ? $("#sop").addClass("successMessage")
                    : (val == 5) ? $("#lor").addClass("successMessage")
                        : (val == 6) ? $("#cgpa").addClass("successMessage")
                            : "";
}