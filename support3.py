class Bicycle(object):
    def __init__ (self, ide, model, color, size, company_inventory):
        self.ide = ide
        self.model = model
        self.color = color
        self.size = size
        company_inventory.append(ide)
    
    def __str__(self):
        s = "ID:{}\tMODEL:{}\t COLOR:{}\t SIZE:{}"
        return s.format(self.ide, self.model, self.color, self.size)

def sample_bicycle_library(bicycles, company_inventory):
    bicycles[0] = Bicycle (0, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[1] = Bicycle (1, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[2] = Bicycle (2, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[3] = Bicycle (3, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[4] = Bicycle (4, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[5] = Bicycle (5, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[6] = Bicycle (6, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[7] = Bicycle (7, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[8] = Bicycle (8, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[9] = Bicycle (9, 'M1', 'Brown', 'Large', company_inventory) 
    bicycles[10] = Bicycle (10, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[11] = Bicycle (11, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[12] = Bicycle (12, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[13] = Bicycle (13, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[14] = Bicycle (14, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[15] = Bicycle (15, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[16] = Bicycle (16, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[17] = Bicycle (17, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[18] = Bicycle (18, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[19] = Bicycle (19, 'M1', 'Black', 'Large', company_inventory) 
    bicycles[20] = Bicycle (20, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[21] = Bicycle (21, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[22] = Bicycle (22, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[23] = Bicycle (23, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[24] = Bicycle (24, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[25] = Bicycle (25, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[26] = Bicycle (26, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[27] = Bicycle (27, 'M1', 'Black', 'XXLarge', company_inventory) 
    bicycles[28] = Bicycle (28, 'Mountain 100', 'Brown', 'Large', company_inventory) 
    bicycles[29] = Bicycle (29, 'Mountain 100', 'Brown', 'Large', company_inventory) 
    bicycles[30] = Bicycle (30, 'Mountain 100', 'Brown', 'Large', company_inventory) 
    bicycles[31] = Bicycle (31, 'Mountain 100', 'Brown', 'Large', company_inventory) 
    bicycles[32] = Bicycle (32, 'Mountain 100', 'Brown', 'Large', company_inventory) 
    bicycles[33] = Bicycle (33, 'Mountain 100', 'Black', 'Large', company_inventory) 
    bicycles[34] = Bicycle (34, 'Mountain 100', 'Black', 'Large', company_inventory) 
    bicycles[35] = Bicycle (35, 'Mountain 100', 'Black', 'Large', company_inventory) 
    bicycles[36] = Bicycle (36, 'Mountain 100', 'Black', 'Large', company_inventory) 
    bicycles[37] = Bicycle (37, 'Mountain 100', 'Black', 'Large', company_inventory) 
    bicycles[38] = Bicycle (38, 'Mountain 100', 'Black', 'XXLarge', company_inventory) 
    bicycles[39] = Bicycle (39, 'Mountain 100', 'Black', 'XXLarge', company_inventory) 
    bicycles[40] = Bicycle (40, 'Mountain 100', 'Black', 'XXLarge', company_inventory) 
    bicycles[41] = Bicycle (41, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[42] = Bicycle (42, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[43] = Bicycle (43, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[44] = Bicycle (44, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[45] = Bicycle (45, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[46] = Bicycle (46, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[47] = Bicycle (47, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[48] = Bicycle (48, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[49] = Bicycle (49, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[50] = Bicycle (50, 'C1', 'Yellow', 'Medium', company_inventory) 
    bicycles[51] = Bicycle (51, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[52] = Bicycle (52, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[53] = Bicycle (53, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[54] = Bicycle (54, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[55] = Bicycle (55, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[56] = Bicycle (56, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[57] = Bicycle (57, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[58] = Bicycle (58, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[59] = Bicycle (59, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[60] = Bicycle (60, 'C1', 'Green', 'Medium', company_inventory) 
    bicycles[61] = Bicycle (61, 'C1', 'Green', 'XLarge', company_inventory) 
    bicycles[62] = Bicycle (62, 'C1', 'Green', 'XLarge', company_inventory) 
    bicycles[63] = Bicycle (63, 'C1', 'Green', 'XLarge', company_inventory) 
    bicycles[64] = Bicycle (64, 'C1', 'Green', 'XLarge', company_inventory) 
    bicycles[65] = Bicycle (65, 'C1', 'Green', 'XLarge', company_inventory) 
    bicycles[66] = Bicycle (66, 'City 100', 'Yellow', 'Medium', company_inventory) 
    bicycles[67] = Bicycle (67, 'City 100', 'Yellow', 'Medium', company_inventory) 
    bicycles[68] = Bicycle (68, 'City 100', 'Yellow', 'Medium', company_inventory) 
    bicycles[69] = Bicycle (69, 'City 100', 'Yellow', 'Medium', company_inventory) 
    bicycles[70] = Bicycle (70, 'City 100', 'Yellow', 'Medium', company_inventory) 
    bicycles[71] = Bicycle (71, 'City 100', 'Green', 'Medium', company_inventory) 
    bicycles[72] = Bicycle (72, 'City 100', 'Green', 'Medium', company_inventory) 
    bicycles[73] = Bicycle (73, 'City 100', 'Green', 'Medium', company_inventory) 
    bicycles[74] = Bicycle (74, 'City 100', 'Green', 'Medium', company_inventory) 
    bicycles[75] = Bicycle (75, 'City 100', 'Green', 'Medium', company_inventory) 
    bicycles[76] = Bicycle (76, 'City 100', 'Green', 'XLarge', company_inventory) 
    bicycles[77] = Bicycle (77, 'City 100', 'Green', 'XLarge', company_inventory) 
    bicycles[78] = Bicycle (78, 'City 100', 'Green', 'XLarge', company_inventory) 
    bicycles[79] = Bicycle (79, 'H1', 'Blue', 'Small', company_inventory) 
    bicycles[80] = Bicycle (80, 'H1', 'Blue', 'Small', company_inventory) 
    bicycles[81] = Bicycle (81, 'H1', 'Blue', 'Small', company_inventory) 
    bicycles[82] = Bicycle (82, 'H1', 'Blue', 'Small', company_inventory) 
    bicycles[83] = Bicycle (83, 'H1', 'Blue', 'Small', company_inventory) 
    bicycles[84] = Bicycle (84, 'H1', 'Red', 'Small', company_inventory) 
    bicycles[85] = Bicycle (85, 'H1', 'Red', 'Small', company_inventory) 
    bicycles[86] = Bicycle (86, 'H1', 'Red', 'Small', company_inventory) 
    bicycles[87] = Bicycle (87, 'H1', 'Red', 'Small', company_inventory) 
    bicycles[88] = Bicycle (88, 'H1', 'Red', 'Small', company_inventory) 
    bicycles[89] = Bicycle (89, 'H1', 'Blue', 'Large', company_inventory) 
    bicycles[90] = Bicycle (90, 'H1', 'Blue', 'Large', company_inventory) 
    bicycles[91] = Bicycle (91, 'H1', 'Blue', 'Large', company_inventory) 
    bicycles[92] = Bicycle (92, 'H1', 'Blue', 'Large', company_inventory) 
    bicycles[93] = Bicycle (93, 'H1', 'Blue', 'Large', company_inventory) 
    bicycles[94] = Bicycle (94, 'H1', 'Red', 'Large', company_inventory) 
    bicycles[95] = Bicycle (95, 'H1', 'Red', 'Large', company_inventory) 
    bicycles[96] = Bicycle (96, 'H1', 'Red', 'Large', company_inventory) 
    bicycles[97] = Bicycle (97, 'H1', 'Red', 'Large', company_inventory) 
    bicycles[98] = Bicycle (98, 'H1', 'Red', 'Large', company_inventory) 
    bicycles[99] = Bicycle (99, 'Highway 100', 'Blue', 'Small', company_inventory) 
    bicycles[100] = Bicycle (100, 'Highway 100', 'Blue', 'Small', company_inventory) 
    bicycles[101] = Bicycle (101, 'Highway 100', 'Red', 'Small', company_inventory) 
    bicycles[102] = Bicycle (102, 'Highway 100', 'Red', 'Small', company_inventory) 
    bicycles[103] = Bicycle (103, 'Highway 100', 'Blue', 'Large', company_inventory) 
    bicycles[104] = Bicycle (104, 'Highway 100', 'Blue', 'Large', company_inventory) 
    bicycles[105] = Bicycle (105, 'Highway 100', 'Red', 'Large', company_inventory) 
    bicycles[106] = Bicycle (106, 'Highway 100', 'Red', 'Large', company_inventory)