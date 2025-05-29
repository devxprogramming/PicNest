# 🏡 PicNest

**Conjures a cozy "nest" where your pictures live safely.**

PicNest is an elegant and secure photo management application designed to transform how you organize, store, and access your digital memories. Built with a focus on simplicity and user experience, PicNest provides a sophisticated yet intuitive platform where your photos find their perfect home.

## ✨ Features

**Secure Upload System**  
Upload your images with confidence through our robust backend infrastructure that prioritizes data integrity and security.

**Intelligent Organization**  
Automatically categorize and organize your photos for effortless browsing and retrieval of your cherished memories.

**Responsive Design**  
Enjoy a seamless experience across all devices, from desktop workstations to mobile phones, with our adaptive interface.

**User Authentication**  
Protect your personal gallery with comprehensive security measures including secure login mechanisms and user session management.

**Scalable Architecture**  
Built to accommodate growing photo collections without compromising performance or user experience.

**Cross-Platform Compatibility**  
Access your photo collection from anywhere, on any device, with consistent functionality and appearance.

## 🚀 Getting Started

### Prerequisites

Before installing PicNest, ensure your system meets the following requirements:

- **Python 3.8 or higher** - Core runtime environment
- **Node.js and npm** - For frontend dependencies and build processes
- **[uv](https://github.com/astral-sh/uv)** - Modern Python dependency management tool

### Installation

**Clone the Repository**
```bash
git clone https://github.com/devxprogramming/PicNest.git
cd PicNest
```

**Backend Setup**
```bash
# Install Python dependencies using uv
uv sync

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run database migrations
python manage.py migrate

# Create a superuser account
python manage.py createsuperuser
```

**Frontend Setup**
```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Build the frontend assets
npm run build
```

**Launch the Application**
```bash
# Start the backend server
python manage.py runserver

# In a separate terminal, start the frontend development server
cd frontend
npm run dev
```

The application will be accessible at `http://localhost:8080` with the API available at `http://localhost:8000`.

## 🛠️ Technology Stack

**Backend Infrastructure**
- Python with Django framework for robust server-side functionality
- RESTful API design for seamless frontend-backend communication
- Secure authentication and authorization systems

**Frontend Experience**
- Modern JavaScript framework with responsive design principles
- Intuitive user interface optimized for photo management workflows
- Progressive Web App capabilities for enhanced mobile experience

**Data Management**
- Efficient database schema optimized for image metadata storage
- Scalable file storage solutions supporting various image formats
- Automated backup and recovery systems

## 📁 Project Structure

```
PicNest/
├── backend/                 # Django backend application
│   ├── picnest/            # Main application directory
│   ├── api/                # API endpoints and serializers
│   ├── authentication/     # User authentication system
│   └── media/              # Uploaded image storage
├── frontend/               # Frontend application
│   ├── src/                # Source code
│   ├── public/             # Static assets
│   └── dist/               # Built application
├── docs/                   # Documentation
├── tests/                  # Test suites
└── requirements/           # Dependency specifications
```

## 🔧 Configuration

**Environment Variables**

Create a `.env` file in the project root with the following configuration:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/picnest_db

# Security Settings
SECRET_KEY=your-secret-key-here
DEBUG=False

# File Storage
MEDIA_ROOT=/path/to/media/storage
MEDIA_URL=/media/

# API Configuration
API_BASE_URL=http://localhost:8000/api/v1/
```

**Additional Configuration**

Customize your PicNest installation by modifying the configuration files located in the `config/` directory. These files control various aspects of the application including upload limits, supported file formats, and user permissions.

## 🤝 Contributing

We welcome contributions from the community to help make PicNest even better. Whether you're fixing bugs, adding new features, or improving documentation, your contributions are valued.

**Development Workflow**

1. Fork the repository and create a feature branch
2. Make your changes following our coding standards
3. Add or update tests as necessary
4. Submit a pull request with a clear description of your changes

**Code Standards**

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Include comprehensive docstrings for all public methods
- Maintain test coverage above 80%

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for complete details.

## 🙋‍♂️ Support

For questions, bug reports, or feature requests, please visit our [Issues](https://github.com/devxprogramming/PicNest/issues) page on GitHub. We strive to respond to all inquiries within 48 hours.

**Community Resources**
- [Documentation](https://github.com/devxprogramming/PicNest/wiki)
- [Discussions](https://github.com/devxprogramming/PicNest/discussions)
- [Release Notes](https://github.com/devxprogramming/PicNest/releases)

---

**Built with ❤️ by the PicNest Team**

*Creating safe, beautiful spaces for your digital memories.*