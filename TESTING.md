# Testing and Validation

## Mannual Testing

Mannual testing was carried on all user storie that were implmented.

![Page 1](documentation/images/mannual_testing_page1.png)
![Page 2](documentation/images/mannual_testing_page2.png)
![Page 3](documentation/images/mannual_testing_page3.png)
![Page 4](documentation/images/mannual_testing_page4.png)
![Page 5](documentation/images/mannual_testing_page5.png)

## Responsive Design

Responsive design testing was carried out on all simulated devices available on Google Chrome dev tools and the website was responsive on all devices.

I also tested the responsiveness on my own phone which is an iPhone 11.

Some examples include:

- [Samsung 8](documentation/images/samsung8_validator.png)
- [iPhoneSE](documentation/images/iPhoneSE_responsive.png)
- [Nest Hub Max](documentation/images/nest_hub_max_responsive.png)
- [iPhone12](documentation/images/iphone12_responsive.png)

## Browser Compatibility

I tested the website on Chrome desktop and Edge desktop. No issues found on either unless already called out in the bug section.

## Performance Testing

### Lighthouse Testing

Lighthouse testing was completed using Chrome dev tools on all the main pages of the website. Some low scores due to heavy load on the page due to images. I need to do some reading on images and how best to handle them in general as a couple of image related issues have popped up during this project.

- [Index page](documentation/images/lighthouse_index_page.png)
- [Articles page](documentation/images/lighthouse_articles_page.png)
- [Article detail page](documentation/images/lighthouse_article_detail_page.png)
- [Sign Up page](documentation/images/lighthouse_sign_up_page.png)
- [Sign In page](documentation/images/lighthouse_sign_in_page.png)
- [Add post](documentation/images/lighthouse_add_post.png)

### Jigsaw validator testing for CSS

- [CSS validation](documentation/images/jigsaw_validator.png)

### Python Testing

Python validation using [CI Python Linter](https://pep8ci.herokuapp.com/). There are some errors on the views.py on the IDE. I have reserched them and most articles are saying its the IDE being fussy and to try # noqa, which I did and it didnt work. Error message is 'Class 'Post' has no 'objects' member.

Results from other py files below:

- [Admin.py](documentation/images/admin.py_validation.png)
- [Apps.py](documentation/images/apps.py_validator.png)
- [Forms.py](documentation/images/forms.py_validator.png)
- [Models.py](documentation/images/models.py_validator.png)
- [Urls.py](documentation/images/blog_urls.py_validator.png)
- [views.py](documentation/images/views.py_validator.png)

## Bugs 

There are currently 3 bugs recorded on the GitHub project board in the to do column.

Logged bugs:

- Disney card image on index page not displaying correctlt. This isnt only this imaage, if any of the other images end up in this card the image renders the same as the Disney one is currently.
- The alert messages push down the hero container then they display on the index page.
- The heart icon and comment icon need to be relooked at current display doesnt look good.

Bugs still to be logged:

- Red call to action buttons and error handling on fomrs are hard to read against the pink background.
- I originally had a placehlder image on the post model but it was overriding the featured images so I removed the placeholder meaning that now an image is mandatory when adding a post so that is annoying for the user.
- I would like to note that after doing the features section of the read me I then carried out the lighthouse testing and I had to change a few colours like remove the green nabar so screenshots to current site look diferent. I also removed the logo as that was also flagging on the lighthouse testing.
- I would also like to acknowledge that some of my commits were massive, particularly 70 & 88 to mention two, commit messages are something I am really trying to be more concious of but sometimes I just lose mysllf in editing too many things at the same time.

