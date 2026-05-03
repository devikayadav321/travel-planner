Wandr is a mobile-first AI-powered travel planning application designed to generate personalized trip suggestions based on user preferences such as destination, budget, duration, and travel style.

This repository currently contains the frontend MVP (HTML/CSS/JS) for trip creation and suggestion flow, with a roadmap toward a full-stack system.

🚀 Features (Current MVP)

✅ Trip Planning Form

Input origin and destination

Select trip type (Solo, Family, Friends, Business)

Define number of travelers and duration

Budget input with validation

✅ Interactive UI

Clean responsive design

Trip type selection with visual feedback

Error handling with inline messages

✅ Navigation Flow

Plan → Suggestions page transition

Session-based data passing 

Basic authentication guard using localStorage

 Project Structure

├──index.html          # Introduction 

├──signup.html         # User signup

├── login.html         # User login 

├──home.html           # The dashboard of the app

├── plan_trip.html     # Trip creation form

├── suggestions.html   # Suggestions display page

How It Works (Current Flow)

1. User fills trip form

2. 

tripData =

{

  from,

  to,

  

  people,

  

  days,

  

  budget,

  

  type

  

}

3. Data stored temporarily

sessionStorage.setItem('navData', JSON.stringify(tripData));

4. Redirect to suggestions page

window.location.href = 'suggestions.html';

5. Suggestions page reads data

const data = JSON.parse(sessionStorage.getItem('navData'));
