#!/usr/bin/python3
#  Author: Daniel Guns
#  Date: Oct 26 2022
import random


terms_to_learn = {'data modeling':'The process of creating a specific date model for a detrmind problem domain.',
                    'entity': 'A person, place,thing, concept, or event for which data can be stored. see also attribute.',
                    'data model': 'A representation, usually graphic, of a complex real-world data structure.\n Data models are used in the databse design phase of the DAtabase life cycle.',
                    'attribute' : 'A characteristic of an entity or object. An attribute has a name and a data type.',
                    'business rule' : 'A description of a policy, procedure, or principle within an organization.\n For example, a pilot cannot be on duty for more then 10 hours durig a 24 hour period,\n or a professor may teach up to four classes a semester. ',
                    'relationship' : 'An association between entities.',
                    'one to many' : ' Associations among two or more entities that are used by data models.\n in a 1:m relationship one entitiy instance is associated with many instance of the related entitity.',
                    'many to many' : 'Association among two or more entities in which one occurance of an entity is associated\n with many occurences of a related entity and one occurance of the relatid entity\n is associated with many occurences of the first entity.' , 
                    'hierarchical model' : 'An early database model whose basic concepts and characteristics\n formed the basis for susequent database develepmoent. \n This model is based on an uside-down tree structure in which each record is called a segment.\n Each segment has a 1:m relationship to the segment directly below it.', 'segment' : 'In the hierarchical data model the equivalent of a file systems record type.' ,
                    'one to one' : 'Associations among two or more entities that are used by date models.\n In a 1:1 relationsip, one entity instance is associated with only one instance of the related entitiy.',
                    'network model' : 'An early data model that represented data as a collection of record types in 1:m relationships.',
                    'constraint': 'A restriction placed on data, usually expressed in the form of rules. For example,\n "A students gpa must be between 0.00 and 4.00"',
                    'ddl' : 'Data definition language. The language that allows a database administrator to define\n the database structure, schema, and subschema. ',
                    'dml' : 'Data manipulation language - The set of commands that allows an end user to manipulate the data in the database,\n such as, SELECT, INSERT, UPDATE, COMMIT, and ROLLBACK.',
                    'schema' : 'A logical grouping of database objects, such as tables, indexes, views, and queries,\n that are related to eachother.',
                    'subschema' : 'The portion of the database that interacts with application programs. ',
                    'relational model' : 'Developed by E.F. Codd of IBM in 1970, the relational model is based on mathematicl\n set theory and repesents data as indidependat relations.\n  Each relation(table) is conceptually represented as a two dimensional structre of intersecting rows and columns.\n The relations are related to each other through the sharing of a common entitity characteristics. \n(values in columns.)',
                    'table': 'A logical construct perceived to be a two[1]dimensional structure composed of intersecting rows\n (entities) and columns (attributes)\n that represents an entity set in the relational model.',
                    'tuple': 'In the relational model, a table row.',
                    'rdbms' : 'A collection of programs that manages a relational database.\n The RDBMS software translates a user’s logical requests (queries)\n into commands that physically locate and retrieve the requested data.' ,
                    'relational diagram' : 'A graphical representation of a relational database’s entities,\n the attributes within those entities, and the relationships among the entities.',
                    'object oriented data model' : 'A data model whose basic modeling structure is an object.',
                    'object' : 'An abstract representation of a real-world entity that has a unique identity,\n embedded properties, and the ability to interact with other objects and itself.',
                    'oodbms' : 'Data management software used to manage data in an object-oriented database model.',
                    'semantic data model' : 'The first of a series of data models that models both data and\n their relationships in a single structure known as an object.',
                    'class' : 'class A collection of similar objects with shared structure (attributes)\n and behavior (methods). A class encapsulates an object’s data representation and a method’s implementation.',
                    'method' : 'In the object-oriented data model, a named set of instructions to perform an action.\n Methods represent real[1]world actions',
                    'class hierarchy': 'The organization of classes in a hierarchical tree in which each parent\n class is a superclass and each child class is a subclass. See also inheritance.',
                    'entity relationship model' : '(ER) model (ERM) A data model that describes relationships (1:1, 1:M, and M:N) among entities at the conceptual level with the help of ER diagrams.',
                    'entity relationship diagram' : 'A diagram that depicts an entity relationship model’s\n entities, attributes, and relations. ',
                    'entity instance': 'A row in a relational table. ',
                    'entity set' : 'A collection of like entities.',
                    'connectivity': 'The type of relationship between entities. Classifications include 1:1, 1:M, and M:N.',
                    'crows foot notation':'A representation of the entity relationship diagram that uses a three-pronged symbol\n to represent the “many” sides of the relationship.',
                    'class diagram notation' : 'The set of symbols used in the creation of class diagrams.',
                    'inheritance' : 'In the object-oriented data model, the ability of an object to inherit the data structure\n and methods of the classes above it in the class hierarchy.',
                    'uml' :'Unified Modeling Language (UML) A language based on object-oriented concepts that provides\n tools such as diagrams and symbols to graphically model a system.',
                    'class diagram' : 'A diagram used to represent data and their relationship in UML object notation.',
                    'extended relational data model' : 'A model that includes the object-oriented model’s best features in an inherently simpler\n relational database structural environment.\n See extended entity relationship model (EERM).',
                    'object relational database managment system':
                    '(O/R DBMS) A DBMS based on the extended relational model (ERDM).\n The ERDM, championed by many relational database researchers, constitutes the relational model’s response to the OODM.\n This model includes many of the object-oriented model’s best features\n within an inherently simpler relational database structure.',
                    'xml' : 'A metalanguage used to represent and manipulate data elements. Unlike other markup languages,\n XML permits the manipulation of a document’s data elements. \nXML facilitates the exchange of structured documents such as orders and invoices over the Internet.',
                    'big data': 'A movement to find new and better ways to manage large amounts\n of web-generated data and derive business insight from it, while simultaneously providing high performance and\n scalability at a reasonable cost.',
                    '3vs' : 'Three basic characteristics of Big Data databases:\n volume, velocity, and variety',
                    'hadoop' : ' Java-based, open-source, high[1]speed, fault-tolerant distributed storage and \ncomputational framework. Hadoop uses low-cost hardware to create clusters of \nthousands of computer nodes to store and process data.',
                    'hadoop distributed file system' : '(HDFS) A highly distributed, fault-tolerant file storage\n system designed to manage large amounts of data at high speeds.',
                    'name node' : 'One of three types of nodes used in the Hadoop Distributed File System (HDFS). \nThe name node stores all the metadata about the file system. See also client node and data node.',
                    'data node' :'One of three types of nodes used in the Hadoop Distributed File System (HDFS). The \ndata node stores fixed-size data blocks (that could be replicated to other data nodes). See also client node and\n name node.',
                    'client node': 'One of three types of nodes used in the Hadoop Distributed File System (HDFS).\n The client node acts as the interface between the user application and the HDFS. See also name node and data node.',
                    'mapreduce' : 'An open-source application programming interface (API) that provides fast data \nanalytics services; one of the main Big Data technologies that allows organizations to process massive data stores',
                    'ansi' : 'The group that accepted the DBTG recommendations and augmented database standards\n in 1975 through its SPARC committee.',
                    'external model': 'external model The application programmer’s view of the data environment.\n Given its business focus, an external model works with a data subset of the global database schema.',
                    'external schema' : 'The specific representation of an external view; the end user’s \nview of the data environment',
                    'nosql' : 'A new generation of database management systems that is not based on the traditional relational database model',
                    'conceptual model' : 'conceptual model The output of the conceptual design process. \nThe conceptual model provides a global view of an entire database and describes the main data objects, avoiding details.',
                    'conceptual schema': 'conceptual schema A representation of the conceptual model,\n usually expressed graphically. See also conceptual model',
                    'software independence' : 'software independence A property of any model or application that does not depend \non the software used to implement it.',
                    'hardware independence' : 'hardware independence A condition in which a model does not depend on the hardware used\n in the model’s implementation. \nTherefore, changes in the hardware will have no effect on the database design at the conceptual level.',
                    'logical design' : 'logical design A stage in the design phase that matches the conceptual design to the \nrequirements of the selected DBMS and is therefore software[1]dependent. Logical design is used to \ntranslate the conceptual design into the internal model for a selected database management system, such as DB2, \nSQL Server, Oracle, IMS, Informix, Access, or Ingress.',
                    'internal model' : 'internal model In database modeling, a level of data abstraction that adapts the conceptual\n model to a specific DBMS model for implementation. The internal model is the representation of a database as “seen”\n by the DBMS. In other words, the internal model requires a designer to match the conceptual model’s characteristics and\n constraints to those of the selected implementation model.',
                    'internal schema' : 'A representation of an internal model using the database construcs supported by the \nchosedn database.',
                    'logical independence' : 'logical independence A condition in which the internal model can be changed without \naffecting the conceptual model. (The internal model is hardware[1]independent because it is unaffected by the computer on \nwhich the software is installed. Therefore, a change in storage devices or operating systems will not affect the internal \nmodel.)',
                    'physical model' : 'physical model A model in which physical characteristics such as location, path, and format\n are described for the data. The physical model is both hardware- and software[1]dependent. See also physical design.',
                    'physical independence' : 'physical independence A condition in which the physical model can be changed without \naffecting the internal model'
                    }


knowterm = 0

totaltries = 0

items = list(terms_to_learn.items())
random.shuffle(items)
for key, value in items:
    proceed = input("Press enter to see a definition, 0 to quit:")
    if proceed != '0':
        print(key + "\n")
        seeterm = input("Hit enter to see the definiton: ")
        if seeterm != '0':
            print(key + ":\n" + value + "\n")
            learn = input("Did you know this term? hit 1 for yes 2 for no: ")
            if learn == '1':
                knowterm = knowterm + 1
                totaltries = totaltries +1

            if learn == '2':
                
                totaltries = totaltries + 1
        else:
            break
    else:
        break


score = knowterm / totaltries
score = score * 100
print("You scored " + str(int(score))+ '%') 






