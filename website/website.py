from flask import Flask, request, render_template, url_for, redirect
import twitterAPIexercise

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()

    try:
        valid_tweetfeed = twitterAPIexercise.get_all_tweets(processed_text)

        # Only calls subsequent functions if media download from twitter feed was successful
        if (valid_tweetfeed):
            twitterAPIexercise.lable_images()
            twitterAPIexercise.make_video()
    except Exception as e:
        print(str(e))
    else:
        if (valid_tweetfeed):
            print("Done. Program successful")
        else:
            print("ERROR: Unable ro run program for the selected twitter feed.\nPlease try again with another username")

    return redirect(url_for('view'))

@app.route('/view')
def view():
    with open("C:/Users/antth/PycharmProjects/EC500Project2/static/imagelabels.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    your_list = [x.strip() for x in content]

    return render_template('output.html', your_list=your_list)

if __name__ == "__main__":
    app.run()

