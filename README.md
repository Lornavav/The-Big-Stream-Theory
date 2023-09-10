# The Big Stream Theory

*I AM RESPONSIVE TO GO HERE*

[View live website](https://the-big-stream-theory-92a5f2837220.herokuapp.com/)

[View admin site](https://the-big-stream-theory-92a5f2837220.herokuapp.com/admin/login/?next=/admin/)


## Introduction

The Big Stream Theory is a website for televison enthusiasts. There is so much to watch theses days and with so many streaming sites available to us.
This website provides articles on Tv shows available on four of the the main streaming sites. Its a place where people can go and look at reviews on the latest TV shows.

Anybody can go and look at the website and the articles. Only logges in users can like articles and leave comments. All comments are subject to approval by website staff. Comments can be approved from the admin panel of the website.

Staff can log into the front end and create, update and delete articles.

### Project Goals

To create a repository of great blog articles about current TV shows on popular streaming sites. Where fellow TV lovers can come together and give their opinions and have discussions in the comments section. We want it to be a go to place when people are looking for something to watch and dont want to scroll for hours.

### Entity Relationship Diagram

The ERD was created on [Lucidchart](https://www.lucidchart.com/). It illustrates the relationship between theCategory, Post and Comment models.

![](documentation/images/erd_diagram.png)

## User Experience

This website was designed using the Five Planes of UX

### Strategy

User stories were written using GitHub Issues and were prioritised using the MoSCoW method. User stories along with testing can be found HERE 

### Scope

The project was scope was to implement CRUD functionaility for the user. This was implmented at at a staff level. Staff can Create articles, Read articles, Update articles and Delete articles. 

### Structure

We kept a simple structure to the website so it is easy for the user to navigate. Using the base template to create a navbar and footer that follows through through the website. Menu items are easy to navigate to. We used cards throughout the website so the user gets used to clicking on these cards for information as they click through the website.

### Skeleton

Desktop wireframes were created at the inital planning stage and the design has varied slightly since due to time constraints and not being able to get the cards to work out the way I had initally planned.

* [Desktop wireframes created with excalidraw](documentation/images/desktop_wireframes.png)

* [Mobile wireframes created with Balsamiq](documentation/images/mobile_wireframes.png)
  
### Surface

I created a logo using [Free Logo Maker](https://www.namecheap.com/) and from there I like the colour scheme and went over to [Coolors](https://coolors.co/) to create the below colour pallette.

![](documentation/images/colour_pallette.png)

## Agile Development

[View project board](https://github.com/users/Lornavav/projects/4)

GitHub Issues and Projects were used to write and manage user stories and epics. The kanban board was used to maage stories into Todo, In Progress and Done columns. I used the MoSCoW method to label Must-Have and Could-Have stories. I did have the intention of adding some Should-Haves but didn't get around to it. I will mention some below in future features.

## Existing Features

### Navigation Bar

The navbar contains a logo and text both hyperlinked to redirect to the home page from any of the other web pages.

There are four  states of the nav bar

* [Logged out state](documentation/images/navbar_logged_out.png)
* [User logggd in](documentation/images/navbar_user.png)
* [Admin logged in](documentation/images/navbar_admin.png)
* [Responsive navbar for mobile](documentation/images/navbar_responsive.png)

### Category Cards

The category cards are displayed on the index.html page. These will help the user navigate to the content they want to see. All cards are clickable and will take the user to the blog post of that category.

* [Category cards index page](documentation/images/category_cards.png)

### Footer

The footer can be viewed from every webpage throughout the side. It contains a contact email for users to get in touch. The social media links all redirect to the relative login pages and these pages will open in a new tab.

* [Footer](documentation/images/footer.png)

### Articles Page

The articles page is where a user can view all articles contained on the website. The page will paginate after 6 articles. The user can click on any article and it will bring them to a page to see further details of the article.

* [Articles page](documentation/images/articles_page.png)

### Article Detail Page

The article detail page shows further details on a single article post. This is where logged in users can leave a comment or like a post. Users who are not logged in will be promted to log in.

* [Article detail page logged in user](documentation/images/article_detail_page.png)
* [Article detail pages not logged in](documentation/images/article_details_not_logged_in.png)

#### Register

The user will be giving the option to register on the website if they are not logged in. This option will appear in the navbar. The user will be directed to a sign up form where they fill in a username, optional email adress and a password.

* [Resgister form](documentation/images/register.png)

### Sign In

Once a user is registered on the website they can use the sign in option to sign into the website.

* [Sign In form](documentation/images/sign_in.png)

### Add Post

Staff have access to add an article post on the front end. When they sign into the website using a staff account they will see the option to add post. Here they can add posts and publish them or leave them as drafts. If they publish the post they will appear straight away on the articles page. If a post is saved as a draft this will not appear anywhere on the website only on the admin panel.

* [Add post](documentation/images/add_post.png)

### Edit Post

Staff have access to edit posts from the front end. The option to edit a post will appear on the articles details page when a staff member is logged into the site.

* [Edit post](documentation/images/edit_post.png)
  
### Delete Post

Staff have access to delete posts from the front end. The option to delete a post will appear on the articles details page when a staff member is logged into the site.

* [Delete post](documentation/images/delete_article.png)

### Messages

Alert messages were implmented with the help of Django messages and message tags. 

## Technologies Used

### Languages

## Testing and Validation

Testing documentation can be found at [TESTING.md](TESTING.md)

## Deployment

### Steps to deploy site using Heroku

### Steps to clone site

## Credits

### Code

### Media

### Acknowledgements