// the webpage needs to dynamically load new changes to the webpage

var sel = document.getElementById("authors");

// find the selected author when chagned. Show all blogs from that author, hide all others
sel.addEventListener('change', () => {
    'use strict';
    var sel = document.getElementById("authors");
    var selectedIndex = sel.selectedIndex;
    var displayAuthor = sel.options[selectedIndex].value;
    if (selectedIndex === 0)
    {
        // if we changed back to the default, show all blogs
        for(var i = 1; i < sel.options.length; ++i)
        {
            var blogs = document.getElementsByClassName(sel.options[i].value);
            for(var j = 0; j < blogs.length; ++j)
            {
                blogs[j].style.display = 'block';
            }
        }
    }
    else
    {
        for(var i = 1; i < sel.options.length; ++i)
        {
            var blogs = document.getElementsByClassName(sel.options[i].value);
            var displayStyle = '';
            if (i === selectedIndex)
            {
                displayStyle = 'block';
            }
            else
            {
                displayStyle = 'none';
            }
            for(var j = 0; j < blogs.length; ++j)
            {
                blogs[j].style.display = displayStyle;
            }
        }
    }
});
