# SCADE Machine Learning API

## :book: Description

Cancer impacted about nearly <b>10 million deaths in the world (WHO) by 2020</b>. One of the most common types of cancer
was skin (non-melanoma) with 1.2 million cases. Skin cancer was common but not everyone was aware of this cancer. Most
people not doing self-diagnoses, they might not understand how to do it periodically. Because of the late action, the
death rate of these cases is still on top of the chart. Through technology, self diagnosis can be provided in an easier
way. This may help to prevent skin cancer and reduce the death rate.

## :star: Minimum Viable Product (MVP)

* User can put image to be classified in cancer class

## :rocket: How To Run

1. The app is combined with docker, make sure your environment support docker too.
1. Launch the app with a simple command ```docker-compose up --build -d```
1. Well done! You are ready to go :partying_face:

## :shamrock: References

1. <b>Convolutional Neural Network</b>
1. <b>Transfer Learning</b>

## :gift: Contributing and Publication

1. We couldn't wait your contribution. Please report the bugs by the issues
1. If you want to send a code. Please send your pull request to us, we would review your code immediately.

## :package: API Docs

1. /predict
   ```text
   HTTP Method : POST
   Query Params : none
   Authorization : none
   Request Body : 
   - Multipart-form
        - field : 
            - skin_image: file
   Response Body : image
   ```
   ![cheers](https://media.giphy.com/media/3KC2jD2QcBOSc/giphy.gif)
   > **wdyt? *this is cool* isn't?**
   >
   > **Scade brings Artificial Intelligence <i>accessible</i> for everyone :sunglasses:**
