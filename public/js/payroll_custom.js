/**
 * Custom JavaScript for Suriname HR/Payroll Module
 * Handles UI interactions and validations
 */

frappe.provide('suriname_hr_payroll');

/**
 * Format currency as SRD
 */
suraname_hr_payroll.format_srd = function(amount) {
    return frappe.format(amount, { fieldtype: 'Currency' }) + ' SRD';
};

/**
 * Validate minimum wage on salary input
 */
suraname_hr_payroll.validate_minimum_wage = function(hourly_rate) {
    const MIN_WAGE = 60.0;
    if (hourly_rate < MIN_WAGE) {
        frappe.msgwarn(__('Hourly rate below minimum wage of SRD {0}', [MIN_WAGE]));
        return false;
    }
    return true;
};

/**
 * Calculate net pay on form
 */
suraname_hr_payroll.calculate_net_pay = function(gross, tax, ss_deduction) {
    return gross - tax - ss_deduction;
};

/**
 * Display payroll summary
 */
suraname_hr_payroll.show_payroll_summary = function(data) {
    const summary = `
        <div class="payroll-summary">
            <h4>Payroll Summary</h4>
            <table class="table table-bordered">
                <tr>
                    <td>Gross Salary</td>
                    <td>${suriname_hr_payroll.format_srd(data.gross)}</td>
                </tr>
                <tr>
                    <td>Income Tax</td>
                    <td>${suriname_hr_payroll.format_srd(data.tax)}</td>
                </tr>
                <tr>
                    <td>Social Security</td>
                    <td>${suriname_hr_payroll.format_srd(data.ss)}</td>
                </tr>
                <tr style="font-weight: bold;">
                    <td>Net Pay</td>
                    <td>${suriname_hr_payroll.format_srd(data.net)}</td>
                </tr>
            </table>
        </div>
    `;
    frappe.msgprint(summary);
};

/**
 * Initialize compliance checks on form load
 */
frappe.ui.form.on('Suriname Salary Slip', {
    onload: function(frm) {
        console.log('Suriname Salary Slip loaded');
    },
    
    refresh: function(frm) {
        if (frm.doc.docstatus === 0) {
            frm.add_custom_button(__('Calculate Pay'), function() {
                frappe.call({
                    method: 'suriname_hr_payroll.doctype.suriname_salary_slip.suriname_salary_slip.calculate_salary',
                    args: { slip_id: frm.doc.name },
                    callback: function(r) {
                        if (r.message) {
                            frm.set_value('net_pay', r.message.net_pay);
                            frm.refresh_field('net_pay');
                        }
                    }
                });
            });
        }
    }
});