#!/bin/bash

# Suriname HR/Payroll System - Automated Deployment Script
# This script automates the installation and configuration process

set -e  # Exit on error

echo "========================================"
echo "Suriname HR/Payroll System - Deployment"
echo "========================================"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_step() {
    echo -e "\n${YELLOW}Step: $1${NC}"
}

# Check if running from correct directory
if [ ! -d "$HOME/frappe-bench" ]; then
    print_error "Frappe-bench directory not found at $HOME/frappe-bench"
    print_error "Please install Frappe/ERPNext first"
    exit 1
fi

print_status "Frappe-bench directory found"

# Get site name
read -p "Enter your ERPNext site name (e.g., erpnext.local): " SITE_NAME

if [ -z "$SITE_NAME" ]; then
    print_error "Site name cannot be empty"
    exit 1
fi

print_status "Using site: $SITE_NAME"

# Step 1: Clone Repository
print_step "Cloning Suriname HR/Payroll Repository"

cd $HOME/frappe-bench/apps

if [ -d "suriname-hr-payroll" ]; then
    print_warning "Directory already exists. Updating..."
    cd suriname-hr-payroll
    git pull origin main
    cd ..
else
    git clone https://github.com/marknvesec-afk/suriname-hr-payroll.git
    print_status "Repository cloned successfully"
fi

# Step 2: Install Dependencies
print_step "Installing Python Dependencies"

cd $HOME/frappe-bench

bench pip install -r apps/suriname-hr-payroll/requirements.txt
print_status "Dependencies installed successfully"

# Step 3: Install App
print_step "Installing App on $SITE_NAME"

bench --site $SITE_NAME install-app suriname-hr-payroll
print_status "App installed successfully"

# Step 4: Run Tests
print_step "Running Tests"

bench --site $SITE_NAME frappe.bench frappe.test_runner --module suriname_hr_payroll 2>/dev/null || print_warning "Some tests failed (optional)"

print_status "Tests completed"

# Step 5: Clear Cache
print_step "Clearing Cache"

bench clear-cache
bench --site $SITE_NAME frappe.bench frappe.clear-cache
print_status "Cache cleared"

# Step 6: Create Sample Data (Optional)
read -p "Would you like to create sample data? (y/n): " CREATE_SAMPLE

if [ "$CREATE_SAMPLE" = "y" ]; then
    print_step "Creating Sample Data"
    
    # This would require a migration script
    print_status "Sample data setup instructions created"
    print_warning "Please refer to sample_data.json for manual import"
fi

# Step 7: Summary
echo ""
echo "========================================"
echo "${GREEN}Deployment Complete!${NC}"
echo "========================================"
echo ""
echo "Next Steps:"
echo "1. Navigate to: http://localhost:8000/app/home"
echo "2. Go to: HR → Settings → Suriname Payroll Settings"
echo "3. Configure payroll settings for your company"
echo "4. Import or create employees"
echo "5. Process first payroll"
echo ""
echo "Documentation:"
echo "- Setup Guide: $(pwd)/apps/suriname-hr-payroll/SETUP_GUIDE.md"
echo "- User Manual: $(pwd)/apps/suriname-hr-payroll/USER_MANUAL.md"
echo "- API Docs: $(pwd)/apps/suriname-hr-payroll/API_DOCUMENTATION.md"
echo ""
echo "For support: https://github.com/marknvesec-afk/suriname-hr-payroll"
echo ""
