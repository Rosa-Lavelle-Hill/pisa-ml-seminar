install.packages("rtools")
if (!require(devtools)) {
  install.packages("devtools")
  require(devtools)
}
install_github("eldafani/intsvy")
library(intsvy)

library(devtools)
install_github("pbiecek/PISA2012lite")

# Main student data
data("student2012", package = "PISA2012lite")
write.csv(student2012, "Data/2012/Students/All.csv")

# Meta data
data("student2012dict", package = "PISA2012lite") 
write.csv(student2012dict, "Data/2012/Students/meta.csv")
library(readr)
meta <- read_csv("Data/2012/Students/meta.csv")
colnames(meta) = c("Column", "Variable_Name")
write.csv(meta, "Data/2012/Students/meta.csv")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Parent data
data("parent2012", package = "PISA2012lite")
write.csv(parent2012, "Data/2012/Parents/All.csv")

# Meta data
data("parent2012dict", package = "PISA2012lite") 
write.csv(parent2012dict, "Data/2012/Parents/meta.csv")
library(readr)
meta <- read_csv("Data/2012/Parents/meta.csv")
colnames(meta) = c("Column", "Variable_Name")
write.csv(meta, "Data/2012/Parents/meta.csv")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# School data
data("school2012", package = "PISA2012lite")
write.csv(school2012, "Data/2012/School/All.csv")

# Meta data
data("school2012dict", package = "PISA2012lite") 
write.csv(school2012dict, "Data/2012/School/meta.csv")
library(readr)
meta <- read_csv("Data/2012/School/meta.csv")
colnames(meta) = c("Column", "Variable_Name")
write.csv(meta, "Data/2012/School/meta.csv")


