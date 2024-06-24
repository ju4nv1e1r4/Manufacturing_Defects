CREATE TABLE Manufacturing_Defects (
    ProductionVolume TEXT 
    ,ProductionCost NUMERIC 
    ,SupplierQuality NUMERIC 
    ,DeliveryDelay TEXT 
    ,DefectRate NUMERIC 
    ,QualityScore NUMERIC 
    ,MaintenanceHours TEXT 
    ,DowntimePercentage NUMERIC 
    ,InventoryTurnover NUMERIC 
    ,StockoutRate NUMERIC 
    ,WorkerProductivity NUMERIC 
    ,SafetyIncidents TEXT 
    ,EnergyConsumption NUMERIC 
    ,EnergyEfficiency NUMERIC 
    ,AdditiveProcessTime NUMERIC 
    ,AdditiveMaterialCost NUMERIC 
    ,DefectStatus TEXT
);

COPY Manufacturing_Defects FROM 'C:\Users\JUAN\Desktop\.begin\tudo\vscode\projects_files\github\Manufacturing_Defects\data\extract\manufacturing_defect_dataset.csv'
DELIMITER ','
HEADER CSV
