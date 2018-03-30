import React, {Component} from 'react';
import ReactDOM from 'react-dom'
import axios from 'axios';

function NoBlogsAvailable() {
    return (
        <p class="lead">
          <a class="btn btn-primary btn-lg" href="/blog/edit/{blog.id}" role="button">Edit</a>
          <a class="btn btn-primary btn-lg" href="/blog/delete/{blog.id}" role="button">Delete</a>
        </p>
    );
}

class Blog extends Component {
    constructor(props){
        super(props);
        this.state = {
            blogs: props.blogs,
            authors: props.authors,
        }
    }

    render() {
        return (
            <div class="container text-left">
                <select id='authors'>
                  <option value="">Select author</option>
                  {this.state.authors.map((author, index) =>
                    <option value={ author.value } key={ index }>{ author.name } </option>
                  )}
                </select>
                {this.state.blogs.map((blog, index) =>
                    <div class={ blog.class + " blog"} key={ index }>
                      <h3 key = {"header" + index}>{blog.blog_title}</h3>
                      <hr class="my-3" key={"hrule-1" + index}/>
                      <p key={"p-1" + index}>{blog.blog_text}</p>
                      <hr key={"hrule-2" + index} class="my-1" />
                      <p key={"p-2" + index}>
                          <strong key={"strong" + index}>{blog.blog_author}</strong> {blog.pub_date}
                      </p>
                      <br key={"br" + index}/>
                  </div>
                )}
            </div>
        );
    }

    componentDidMount() {
        (() => {
            setInterval(() => {
                axios.get('blog/get_blogs').then((response) => {
                    console.log(response.data);
                    const authors = response.data.authors;
                    const blogs = response.data.blogs;
                    this.setState({blogs, authors});
                });
            }, 500);
        })();
  }
}

function BlogView(props)
{
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

