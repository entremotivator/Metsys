import streamlit as st
from PIL import Image
import os

# --- Configuration ---
st.set_page_config(
    page_title="Meticulous Systems Feature Showcase",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Helper Functions ---
def display_image(image_path, caption=""):
    """Displays an image from the local 'images' directory."""
    try:
        img = Image.open(image_path)
        st.image(img, caption=caption, use_container_width=True)
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")

def feature_section(title, features, image_files):
    """Creates a feature section with a title, features, and associated images."""
    st.header(title)
    st.markdown(features)
    
    # Display images in a 3-column layout
    num_cols = min(len(image_files), 3)
    if num_cols > 0:
        cols = st.columns(num_cols)
        # Iterate over the images and assign them to columns cyclically
        for i, file in enumerate(image_files):
            with cols[i % num_cols]:
                display_image(os.path.join("images", file))

# --- Main Application ---
st.title("Meticulous Systems: The All-in-One Digital Platform")
st.markdown(
    """
    **Meticulous Systems** is a fully integrated digital platform designed to streamline your business operations, 
    from course management and project execution to customer relationship management and e-commerce. 
    Explore the tabs below to see the powerful features of this unified system.
    """
)

# --- Tab Definitions ---
tab_titles = [
    "Course Management", 
    "Project & Task Management", 
    "Appointment Scheduling", 
    "Customer Relationship Management", 
    "E-commerce & Sales", 
    "System Integrations & Automation",
    "Page & Layout Design"
]

tabs = st.tabs(tab_titles)

# --- 1. Course Management (LMS) ---
with tabs[0]:
    feature_section(
        "Comprehensive Course Management",
        """
        This module provides a complete solution for building, managing, and delivering online courses. 
        It includes tools for tracking student enrollment, managing instructors, and organizing course content into lessons and quizzes. 
        The system supports a full academic workflow, from content creation to student progress tracking and review management.
        """,
        [
            "IMG_0399.png", # Academy Dashboard
            "IMG_0400.png", # Courses List
            "IMG_0401.png", # Lessons List
            "IMG_0402.png"  # Instructors List
        ]
    )

# --- 2. Project & Task Management ---
with tabs[1]:
    feature_section(
        "Advanced Project & Task Management",
        """
        Organize your work with a robust project management suite. 
        It allows for the creation of active projects with detailed views that include task lists, Kanban boards for visual workflow, 
        Gantt charts for timeline tracking, and dedicated sections for discussions, milestones, and file sharing. 
        This ensures every project stays on track and all team members are aligned.
        """,
        [
            "IMG_0389.png", # Active Projects List
            "IMG_0390.png"  # Task List/Kanban View
        ]
    )

# --- 3. Appointment Scheduling ---
with tabs[2]:
    feature_section(
        "Seamless Appointment Scheduling",
        """
        Manage all your bookings and appointments effortlessly. 
        The system provides a centralized dashboard to monitor appointments, services, employees, and customer bookings. 
        It features highly customizable notification settings, allowing you to send automated email, SMS, and even WhatsApp notifications 
        to both customers and staff for approvals, cancellations, and reminders.
        """,
        [
            "IMG_0377.png", # Appointments Dashboard
            "IMG_0379.png", # Appointments List
            "IMG_0382.png", # Services Management
            "IMG_0386.png"  # Notification Settings
        ]
    )

# --- 4. Customer Relationship Management (CRM) ---
with tabs[3]:
    feature_section(
        "Integrated Customer Relationship Management",
        """
        Gain a 360-degree view of your customers with the integrated CRM. 
        The dashboard tracks active contacts, email campaigns, and automation performance. 
        It allows for detailed contact management, including tagging, list segmentation, and dynamic grouping. 
        The system supports full email marketing capabilities with sequences and templates to nurture leads and manage customer journeys.
        """,
        [
            "IMG_0392.png", # CRM Dashboard
            "IMG_0394.png"  # Contact Profile View
        ]
    )

# --- 5. E-commerce & Sales ---
with tabs[4]:
    feature_section(
        "Powerful E-commerce and Sales Platform",
        """
        Run your online store with a comprehensive e-commerce solution. 
        The platform offers a sales performance overview, tracking net sales, orders, and product variations sold. 
        It includes full product management with inventory control, category and attribute organization, and a dedicated customer section 
        to view order history and lifetime spend.
        """,
        [
            "IMG_0376.png", # E-commerce Overview
            "IMG_0371.png", # All Products List
            "IMG_0369.png"  # Customers List
        ]
    )

# --- 6. System Integrations & Automation ---
with tabs[5]:
    feature_section(
        "Hundreds of System Integrations and Automations",
        """
        The core strength of Meticulous Systems lies in its ability to connect all your tools. 
        It features a massive library of pre-built integrations with popular forms, membership systems, page builders, and other services. 
        This powerful automation engine allows you to create complex workflows, ensuring data flows seamlessly between all components of your system and external applications.
        """,
        [
            "IMG_0397.png" # Integrations List
        ]
    )

# --- 7. Page & Layout Design (Page Builder) ---
with tabs[6]:
    feature_section(
        "Intuitive Page and Layout Design",
        """
        Create stunning, professional websites without writing a single line of code. 
        The visual drag-and-drop page builder provides complete control over your site's design. 
        Key features include a vast library of pre-designed templates, responsive design controls for perfect display on any device, 
        and the ability to create global elements and styles for consistent branding across your entire site.
        """,
        [] # No specific screenshot provided, relying on text description
    )

# --- Final Step: Expose the port for the user to view ---
st.sidebar.markdown("---")
st.sidebar.info("The application is running and ready to be viewed.")
