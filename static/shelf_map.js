$('#email').click(function () {
    alert('snulibmap@gmail.com');
});

var pivots_list = [
    { room_num: 1, pivots:
                [{left: 92, top: 64, row: 1, col: 'A'},
                {left: 280, top: 64, row: 1, col: 'H'},
                {left: 280, top: 444, row: 9, col: 'H'}]},
    { room_num: 2, pivots:
                [{left: 85, top: 50, row: 1, col: 'A'},
                {left: 275, top: 50, row: 1, col: 'H'},
                {left: 89, top: 890, row: 25, col: 'A'},
                {left: 275, top: 50, row: 31, col: 'H'}]},
    { room_num: 3, pivots:
                [{left: 75, top: 35, row: 1, col: 'A'},
                {left: 325, top: 35, row: 1, col: 'K'},
                {left: 325, top: 805, row: 23, col: 'K'}]},
    { room_num: 4, pivots:
                [{left: 80, top: 65, row: 1, col: 'A'},
                {left: 330, top: 65, row: 1, col: 'K'},
                {left: 330, top: 605, row: 15, col: 'K'}]},
    { room_num: 5, pivots:
                [{left: 80, top: 65, row: 1, col: 'A'},
                {left: 370, top: 662, row: 24, col: 'M'}]},
    { room_num: 6, pivots:
                [{left: 85, top: 65, row: 1, col: 'A'},
                {left: 373, top: 65, row: 1, col: 'M'},
                {left: 280, top: 444, row: 26, col: 'M'}]},
    { room_num: 7, pivots:
                [{left: 60, top: 40, row: 1, col: 'A'}]}
];

function find_pivot(room_num, row, col) {
    var pivots = pivots_list[room_num-1].pivots;
    // find pivot from right bottom side
    for (var i = pivots.length - 1; i >= 0; i--) {
        var pivot = pivots[i];
        if (row >= pivot.row && col >= pivot.col) {
            return pivot;
        }
        else {
            continue;
        }
    }
}

function render_map(room_num, row, col, name) {
    var pivot = find_pivot(room_num, row, col);
    var offset_left = col.charCodeAt(0) - pivot.col.charCodeAt(0);
    var offset_top = row - pivot.row;
    var left = pivot.left + offset_left * 20;
    var top = pivot.top + parseInt(offset_top) * 35 + (row.endsWith('.5') ? 10 : 0); // 0.5 handling

    $("#modal_title").text(name);
    var modal_body = $("#modal_body");
    modal_body.html(''); // delete existing image
    var src = '/media/archive' + room_num + '.png';
    var img = $('<img />');
    img.attr("src", src).appendTo(modal_body);
    $('<span class="marker"/>').css({left: left, top: top}).appendTo(modal_body);
}