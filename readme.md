# GlobalVibes Blogging System

Welcome to the GlobalVibes Blogging System, a feature-rich and dynamic blogging platform built with Django, Tailwind CSS, CKEditor and jQuery Ajax. This system provides users with a seamless experience, incorporating advanced features such as user-friendly notifications, categorized blogs, and interactive communities.

## Features

### User Accounts

- **Custom User Model:**
  - Users can upload profile images.
  - Promoter status updates automatically upon admin approval.
  - Email login for enhanced security.
  - Unique usernames and passwords.

### Notifications

- **Notification System:**
  - Push notifications for various actions within the system.
  - Centralized Notification model for easy access.
  - Notification count for users.
  - Mark notifications as read/unread.
  - Notification links for quick access to relevant content.

### Blogging

- **Categories and Tags:**

  - Categorize blogs with the Category model.
  - Add tags for better content organization.
- **Blog Model:**

  - Title, content, and cover image for expressive blogs.
  - Categorized and tagged for easy retrieval.
  - Comments and likes for user interaction.
- **Commenting System:**

  - Users can reply to comments using '@username'.
  - Share button for quick copying of blog URLs.
- **Filtering Options:**

  - Sort blogs by today's, yesterday's posts.
  - Filter by category, tags, and date range.
  - Search blogs using various fields.

### Promoters

- **Promoters App:**
  - Promoters can create, manage blogs and communities.
  - Admin approval required to become a promoter.

### Community Interaction

- **Community Model:**

  - Create communities with titles, cover images, and descriptions.
- **Chatting System:**

  - Real-time chat within communities.
  - Admins/promoters can create/delete communities and approve user requests.

## Getting Started

1. **Installation:**

   - Clone the repository: `git clone <https://github.com/Levi-Chinecherem/GlobalVibes.git>`
   - Install dependencies: `pip install -r requirements.txt`
2. **Database Setup:**

   - Apply migrations: `python manage.py migrate`
3. **Run the Development Server:**

   - Start the server: `python manage.py runserver`
4. **Access the Application:**

   - Open your browser and go to `http://127.0.0.1:8000/`
5. **Explore and Contribute:**

   - Dive into the codebase, explore the features, and contribute to the project's growth.

## Contributors

- Add your name here if you contribute!

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the any contributor and anyone from the open-source community that will support.

Start exploring and happy blogging with GlobalVibes!
