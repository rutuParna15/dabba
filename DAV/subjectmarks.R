# Define subjects and corresponding marks
subjects <- c("English", "Science", "Maths", "History")
marks <- c(70, 90, 80, 74)

# Plotting the bar chart
barplot(marks,
        names.arg = subjects,
        col = "skyblue",
        main = "Student Marks in Subjects",
        xlab = "Subjects",
        ylab = "Marks",
        ylim = c(0, 100))

# Calculating the average
average_marks <- mean(marks)

# Print the average
cat("Average Marks:", average_marks, "\n")
