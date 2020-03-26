# aws-data-exchange-usa-hospital-beds
Data on numbers of licensed beds, staffed beds, ICU beds, and the bed utilization rate for the hospitals in the United States

## More Information:
- Source: [Definitive Healthcare](https://coronavirus-disasterresponse.hub.arcgis.com/datasets/definitivehc::definitive-healthcare-usa-hospital-beds?geometry=94.394%2C-16.820%2C-119.356%2C72.123&where=UPPER(HQ_STATE)%20like%20%27%25IL%25%27%20AND%20UPPER(COUNTY_NAME)%20like%20%27%25LAKE%25%27)  
- Frequency: Daily

Please see the following for more details about each metric in the dataset:

**Number of Licensed beds:**  is the maximum number of beds for which a hospital holds a license to operate; however, many hospitals do not operate all the beds for which they are licensed. This number is obtained through DHC Primary Research. Licensed beds for Health Systems are equal to the total number of licensed beds of individual Hospitals within a given Health System.

**Number of Staffed Bed:**  is defined as an "adult bed, pediatric bed, birthing room, or newborn ICU bed (excluding newborn bassinets) maintained in a patient care area for lodging patients in acute, long term, or domiciliary areas of the hospital."  Beds in labor room, birthing room, post-anesthesia, postoperative recovery rooms, outpatient areas, emergency rooms, ancillary departments, nurses and other staff residences, and other such areas which are regularly maintained and utilized for only a portion of the stay of patients (primarily for special procedures or not for inpatient lodging) are not termed a bed for these purposes.  Definitive Healthcare sources Staffed Bed data from the Medicare Cost Report or Proprietary Research as needed. As with all Medicare Cost Report metrics, this number is self-reported by providers. Staffed beds for Health Systems are equal to the total number of staffed beds of individual Hospitals within a given Health System.  Total number of staffed beds in the US should exclude Hospital Systems to avoid double counting.  ICU beds are likely to follow the same logic as a subset of Staffed beds.

**Number of ICU Beds - ICU (Intensive Care Unit) Beds:**  are qualified based on definitions by CMS, Section 2202.7, 22-8.2. These beds include ICU beds, burn ICU beds, surgical ICU beds, premature ICU beds, neonatal ICU beds, pediatric ICU beds, psychiatric ICU beds, trauma ICU beds, and Detox ICU beds.

**Bed Utilization Rate:**   is calculated based on metrics from the Medicare Cost Report: Bed Utilization Rate = Total Patient Days (excluding nursery days)/Bed Days Available

**Potential Increase in Bed Capacity:** This metric is computed by subtracting “Number of Staffed Beds from Number of Licensed beds” (Licensed Beds – Staffed Beds). This would provide insights into scenario planning for when staff can be shifted around to increase available bed capacity as needed.

**Hospital Definition:**  Definitive Healthcare defines a hospital as a healthcare institution providing inpatient, therapeutic, or rehabilitation services under the supervision of physicians. In order for a facility to be considered a hospital it must provide inpatient care.

*Hospital types are defined by the last four digits of the hospital’s Medicare Provider Number. If the hospital does not have a Medicare Provider Number, Definitive Healthcare determines the Hospital type by proprietary research.*

### Hospital Types

#### Short Term Acute Care Hospital (STAC)
- Provides inpatient care and other services for surgery, acute medical conditions, or injuries
- Patients care can be provided overnight, and average length of stay is less than 25 days

#### Critical Access Hospital (CAH)
- 25 or fewer acute care inpatient beds
- Located more than 35 miles from another hospital
- Annual average length of stay is 96 hours or less for acute care patients
- Must provide 24/7 emergency care services
- Designation by CMS to reduce financial vulnerability of rural hospitals and improve access to healthcare
- Religious Non-Medical Health Care Institutions
- Provide nonmedical health care items and services to people who need hospital or skilled nursing facility care, but for whom that care would be inconsistent with their religious beliefs

#### Long Term Acute Care Hospitals
- Average length of stay is more than 25 days
- Patients are receiving acute care - services often include respiratory therapy, head trauma treatment, and pain management
- Rehabilitation Hospitals
- Specializes in improving or restoring patients' functional abilities through therapies

#### Children’s Hospitals
- Majority of inpatients under 18 years old

#### Psychiatric Hospitals
- Provides inpatient services for diagnosis and treatment of mental illness 24/7
- Under the supervision of a physician

#### Veteran's Affairs (VA) Hospital
- Responsible for the care of war veterans and other retired military personnel
- Administered by the U.S. VA, and funded by the federal government

#### Department of Defense (DoD) Hospital
- Provides care for military service people (Army, Navy, Air Force, Marines, and Coast Guard), their dependents, and retirees (not all military service retirees are eligible for VA services)


## Contact Information
For more information please visit - https://www.definitivehc.com/ - or contact sales@definitivehc.com. If you have any questions about this listing, please contact info@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.

### Refund Policy  
Refunds Not Applicable
