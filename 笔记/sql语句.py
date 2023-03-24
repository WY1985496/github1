"""

create table test_cases(
    ID int(11) not null primary key AUTO_INCREMENT,
    caseId varchar(50) not null,
    testId varchar(50) not null,
    caseName varchar(50) not null,
    createTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updateTime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    testResult varchar(20)
);



insert into test_cases(caseId, testId, caseName, testResult) values ("caseId", "testId", "caseName", "testResult");

"""
