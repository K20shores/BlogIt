import React from 'react';
import ReactDOM from 'react-dom'
//import './index.css';

function NoBlogsAvailable() {
    return (
        <p class="lead">
          <a class="btn btn-primary btn-lg" href="/blog/edit/{blog.id}" role="button">Edit</a>
          <a class="btn btn-primary btn-lg" href="/blog/delete/{blog.id}" role="button">Delete</a>
        </p>
    );
}

function Blog(props) {
    console.log("Blog props:");
    console.log(props);
    const authors = props.authors;
    const blogs = props.blogs;
    return (
        <div class="container text-left">
            <select id='authors'>
              <option value="">Select author</option>
              {authors.map(author =>
                <option value={ author.value }>{author.name}</option>
              )}
            </select>
            {blogs.map((blog, index) =>
                <div class={ blog.class } key={ index }>
                  <h3>{blog.blog_title}</h3>
                  <hr class="my-3" />
                  <p>{blog.blog_text}</p>
                  <hr class="my-1" />
                  <p><strong>{blog.blog_author}</strong> {blog.pub_date}</p>
                  <br />
              </div>
            )}
        </div>
    );
}

function BlogView(props)
{
    console.log("BlogView props:");
    console.log(props.authors);
    console.log(props.blogs);
    const hasBlogs = props.blogs.length !== 0 ? true : false;
    if (hasBlogs)
    {
        return <Blog authors={props.authors} blogs={props.blogs} />;
    }
    return <NoBlogsAvailable />;
}

ReactDOM.render(
    React.createElement(BlogView, window.props),
    window.react_mount, // a reference to the #react div that we render to
)
